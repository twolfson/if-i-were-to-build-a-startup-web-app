# Django <> React Security and Architecture
This started as a security detour we took while exploring [explorations/4-django-allauth-react-proxy](../explorations/4-django-allauth-react-proxy).

For each of these setups, I'm going to lay out the URL structure, interaction architecture, and security implications.

Since this is inside of `if-i-were-to-build-a-startup-web-app`, I'm going to try to use `django-allauth` from the start since:

- Building our own security is risky (even if we're picking/choosing from other libraries)
- Building our own security adds significant time (e.g. building many authentication pages (login, sign up, password reset, password reset confirm, verify email, corresponding email messages) + their interconnectedness)

## Terminology
- https://app.example.com/ is a URL with the parts of protocol: `https`, subdomain: `app.`, domain: `example.com`, [and more](https://nodejs.org/api/url.html#url-strings-and-url-objects)
    - We'll say origin if it's the whole `app.example.com`
- For 2 URLs to be "same site", we need protocol and domain to be the same
- e.g. https://foo.example.com/ and https://bar.example.com/ are same site but different origin
- e.g. https://foo.example.com/ and https://foo.google.com/ are different site and different origin

## Same origin with proxy
In this setup, Django and React are hosted on the same domain:

- https://app.example.com
    - / - Static webpage for React (hosted by NGINX/similar)
    - /main.abcdef.js, static JS bundle for React (hosted by NGINX/similar)
    - /auth - Proxied route (e.g. NGINX) to Django -> `django-allauth` for authentication (HTML forms using CSRF) (e.g. `/auth/login`, `/auth/signup`)
    - /api - Proxied route to Django -> Django REST Framework for JSON based handling
    - /admin - Proxied route to Django -> Django Admin

We have at least 2 ways to handle the session generated by authentication:

- Cookies
- JSON Web Tokens (JWT)

Cookies are tried and true for servers without any proxy magic. e.g. Techniques to guard them, like CSRF, and the surface area is relatively well known.

When a proxy is added to the mix... we'll get to that shortly.

JWT has some more headaches associated with it, and is much easier to implement incorrectly. That is:

- They should be stored via `HttpOnly` cookies, not `localStorage` or `sessionStorage` (since third party scripts can get compromised + steal these resources)
- Refresh tokens are intended as long-lived but access tokens are short-lived + need regular regeneration, leading to app complexity
- JWT cannot be easily invalidated
- If any metadata is stored in the JWT, then it can also go out of date (since not invalidated)

I'd like to note that in **both these cases, they're vulnerable to CSRF unless we use SameSite**, and SameSite is tricky due to being a modern browser feature, though admittedly [95% adoption][caniuse-SameSite].

The CSRF vulernability comes about even with APIs:

- ~An example CSRF attack with JSON can be crafted like this:~
    - ~https://www.directdefense.com/csrf-in-the-age-of-json/~
        - ~Here's an [example I made to verify](https://codepen.io/twolfson/pen/oNmNLxm)~
        - ~The junk `foo` parameter would typically be discarded by an API, but not reject the entire request. This is because client <> server can often get out of sync/date and it'd compromise user experience~
        - This is quite low risk due to requiring `text/plain` content type
- APIs that are for full web applications will inevitably will need to accept non-JSON content (e.g. change profile photo, upload document)
    - In this scenario, we'd use a [`multipart/form-data`](https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data#the_enctype_attribute) `Content-Type` to avoid excess encoding/decoding work + file size compications
        - We could have workarounds like exposing upload URLs for S3/similar directly, but that leaves the server out of the loop for logic
    - Unfortunately, that opens the door for a CSRF HTML form submitting the same =/
    - Attribution for realization (then I agree with reality), https://systemweakness.com/ways-to-exploit-json-csrf-simple-explanation-5e77c403ede6

[caniuse-SameSite]: https://caniuse.com/same-site-cookie-attribute

With this background established, let's talk through what our plan is + how secure it is

### Cookie based auth
For simplicity, we're going to manage a `logged_in` cookie to establish whether the user is still logged in or not.

This is a non-`HttpOnly` cookie so we avoid exposing our session cookie to third party scripts.

> Initial plan was a `localStorage` setting, but a cookie is way cleaner/more consistent (i.e. no mismatched expirations).

The following is describing how an implementation *should* go (i.e. specification). We've yet to do this in practice.

#### Initial auth
- User visits https://app.example.com/foo/bar
    - React SPA loads and looks for `loggedd_in`
    - It doesn't see it so it redirect to https://app.example.com/auth/login?redirect_uri=/foo/bar
- Browser loads https://app.example.com/auth/login?redirect_uri=/foo/bar
    - Django presents HTML form with CSRF field
- User logs in
    - Django establishes cookie-based session, with `HttpOnly` and `SameSite=strict` set
        - `HttpOnly` is required to prevent third party scripts from stealing `document.cookie`
        - `SameSite` is required for API piece, will explain there
        - On some applications, sessions can be established first. In that case, I'd still expect session id rotation here (to prevent session fixation attack)
    - Django saves user ID to session in DB
    - Django middleware (built by us) also adds identical cookie for `logged_in` except value is "1" and `HttpOnly` is `false`
        - This is a double win for auth handled by Django Admin
    - Django redirects user to https://app.example.com/auth-success?redirect_uri=/foo/bar (Auth0 calls this [`/callback`](https://developer.auth0.com/resources/guides/spa/react/basic-authentication), but I like these semantics more)
- Browser loads https://app.example.com/auth-success?redirect_uri=/foo/bar
    - We parse the query parameter on all pages, but that complicates logic/setup, and there's a possible flash of content while it's handled (this is why Auth0 pushes for this)
    - This page also gives us a common location to capture any relevant events
    - React SPA pushes browser to https://app.example.com/foo/bar

#### API usage
- React SPA makes XHR to https://app.example.com/api/baz
    - Browser uses current cookie, including our session one
    - Django DRF sees the cookie and uses that
    - To mitigate CSRF risk, we need to use `SameSite=strict` when setting the cookie
        - Otherwise, someone could manufacture an HTML form to submit to our API as elaborated above

#### Session expiration
- If the user hasn't interfaced with the app in a while, then their cookie will expire
- User visits https://app.example.com/foo/bar
    - React SPA loads, doesn't see a `logged_in` cookie, and redirects to https://app.example.com/auth/login?redirect_uri=/foo/bar

#### Logout
- When a user navigates to https://app.example.com/logout
    - React SPA redirects to https://app.example.com/auth/logout
- Browser navigates to https://app.example.com/auth/logout
    - (Double check implementation) Django loads, unsets the cookie, and removes the session from the DB
        - Session removal from DB is to prevent session fixation

#### Admin "Login as"
- `django-loginas` is a Django extension which allows logging in as a user via Django Admin
- This is very useful for supporting your team internally
- Intended implementation for us: When the button is pressed
    - It will update the session and cookie to the relevant user
    - Navigate to the redirect URL, which we'll set to our `/auth-success` one
    - `/auth-success` interacts as per usual, treating user as logged in and such

### JWT based auth
The structure required here is roughly the same as cookie based auth, except we sign + set a JWT refresh token as cookie after login -- and Django is still using normal cookie sessions.

To reiterate, this is more work with no added benefit since the JWT is in a HttpOnly cookie (since otherwise it can be scraped), so it's not recommended.

There's even more complexity I'm glossing over around the JWT being stored is the *refresh* token, not the *access* token, meaning even more work is needed on the React side =/

More reading:
- https://blog.logrocket.com/jwt-authentication-best-practices/#whyyoushouldnt
- https://www.loginradius.com/blog/engineering/guest-post/jwt-authentication-best-practices-and-when-to-use/

#### Initial auth
- User visits https://app.example.com/foo/bar
    - React SPA loads, doesn't see `logged_in` non-HttpOnly cookie, and redirects to auth
- Browser loads https://app.example.com/auth/login?redirect_uri=/foo/bar
    - Django establishes cookie-based session, with `HttpOnly` and `SameSite=strict` set (should double check on implementation)
- User logs in
    - With Django's 302 redirect back to https://app.example.com/auth-success?redirect_uri=/foo/bar, we also set an `HttpOnly` + `SameSite=strict` cookie for JWT
- Same flow as above

#### API usage
- React SPA makes XHR to https://app.example.com/api/baz
    - Browser uses current cookie, including the JWT one
    - Django DRF sees the cookie and uses that
- We also need to set up CORS properly due to XHR usage

#### Admin "Login as"
- Same as before but requires extra step to also set said JWT cookie

## Different origin + same site
The rough architecture as above also applies to different origins on the same site.

We need to change from `SameSite=strict` to `SameSite=lax` to allow permission for an XHR to use the cookie, add CORS headers to server responses, and make any XHR use [`withCredentials`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials).

Everything else though is the same.

### Reasons for different origin + same site
I've seen different origin + same site be argued for because it enables things like being pre-configured for CORS, allowing for easy interaction between environments (e.g. develop locally with beta API).

I believe that any configuration done with different domains can also be achieved with same domain + proxy.

- Local development against beta API: Set up React Dev Server to point to beta API, all cookies and such should work as expected
- [Deploy Previews][] (e.g. Netlify): These should support the same kind of proxying as React Dev Server and NGINX, https://docs.netlify.com/routing/redirects/rewrites-proxies/
- CDN for React content:
    - This seems like misplaced priorities since React is still largely going to be talking to the API backend
    - If you're scaling 1 of these, you prob should scale both
- Expose API to customers
    - Both same and different domain versions can be done, but the API you'd expose to customers isn't the same as what you consume
    - Customers expect stability and versioning for theirs
    - Whereas an application API changes rapidly, especially as a startup
    - You'd be building this as a standalone product as-is

[Deploy Previews]: (https://docs.netlify.com/site-deploys/deploy-previews/)

## Same origin with proxy and full React XHR
There's 2 scenarios here:

- If React SPA stays a static page, then you're starting to interact with `django-allauth` as an AJAX entity (leveraging CSRF non-HttpOnly cookie)
    - This requires something to touch the `/auth` URL via AJAX first to ensure a cookie, but that's easily done
        - e.g. `useCsrfCookie()`: Sees if no cookie -> runs `async/await fetch('/auth/login' or build something lighter)` -> reads/returns cookie
    - Once that's done, it still might be tricky to build all the pages + deal with edge cases like mandatory email verification, since that'd be a request at page load (hopefully done in parallel with other requests)
    - In this case, be sure to use `#token=foo` instead of `?token=foo` to avoid leaking to HTTP referrer with third party scripts
- Alternatively, you make Django host React for these pages + React gets the CSRF cookie for free when rendering the page
    - In these scenarios, the flow should work as above (e.g. cookie setting and all) but it leads to headaches with the development web server (e.g. websockets, dynamic bundle hashes)
    - The rest of the points from the React SPA version hold

## Different origin + same site with full React XHR
This will not work because there's no way for React to get the CSRF cookie or rendered HTML to use with `django-allauth` here.

Maybe there's some hack/workaround with a callback URL/endpoint, or setting the cookie domain to the root domain, but that's likely opening the door for further security issues.

As a result, the implementer is likely stuck hacking together their own full security implementation =/

## Different sites
This will not work with cookies or JWT as `HttpOnly` cookies because there's no way to transfer data through those cookies without removing the `SameSite` rule, which opens up CSRF vulnerabilities.

Session can be stored in-memory but this is probably a frustrating end user experience. We don't want to use `localStorage` as it will allow session theft from compromised third party scripts.

## Third party authentication providers
Auth0 and such are viable alternatives to setting up all this handshaking yourself. At the same time, it foregoes a lot of long-term tradeoffs as well as doesn't save that much time (e.g. maybe 2 days).

Tradeoffs include:

- Long-term vendor lock-in for users (very hard to migrate)
- Additional existential risks for company (e.g. risk of abrupt shutdown, uptime limitations)
- Not being able to see user info inside Django admin
- Possible limitations around custom logic/fields

## Recap
- Django hosting `django-allauth` + styling similarly is the sanest path to develop on
    - There might be some code reimplementation, but this is the cost of 2 separate web apps talking to each other
    - and saves a lot compared to reimplementing all of the server side logic + blocking in UI + possible headaches around email verification + etc
    - This is also a normal behavior on many implementations (e.g. common SSO service, or third party ones like Auth0)
- Cookies similarly are the sanest path, vs JWT -- especially since that's stored in a cookie as well
- Same or separate domains with cookies are comparable, though same domain is nicer due to no CORS frustrations + stricter `SameSite` policy
