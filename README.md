# If I Were to Build a Startup Web App

# THIS IS A WORK IN PROGRESS, PLEASE IGNORE THE MESS

- TODO: See TODOs

Choices, explanations, and documentation around if I were to build a startup web app in 2023.

For context, I have 12 years experience at startups (mostly early stage), have been 3x first engineer (including 1x founder), and am a former Uber.

Our goal with these choices is towards building a product as quickly and efficiently as possible.

The information here will go out of date, so take it a grain of salt and as a snapshot in time.

1. First, [Minimum Viable Product (MVP) without web app](README.md#stage-0-minimum-viable-product-mvp-without-web-app)
2. Then, [Betting on product interactivity and deciding aesthetics](README.md#stage-1-initial-build)
    - Assuming basic [CRUDL][] forms with 1-2 isolated pages of high interactivity (e.g. maps, graphs)
    - Bootstrap for off the shelf aesthetics + prebuilt components
3. Then, making further architectural decisions:
    - Rough recommendation:
        - Django with django-allauth
        - Bootstrap
        - Limited custom JS
        - [Additional documents like PostgreSQL and no Docker covered below](#architectural-decisions)
        - TODO: Consider expanding fully?
    - Why this is a rough recommendation:
        - I've used plenty of frameworks with just GET/POST responses and limited JS
        - However, I've never used Django as an HTML form app (was REST API + admin tools) nor django-allauth in a non-trivial manner
            - In our [Explorations document][explorations-django-allauth], we found Django without django-allauth was quite infuriating for self-serve signups
        - so take this advice with a grain of salt
        - TODO: Broader Python templating evaluation/comparison?
            - Mako seems like a winner due to having bare Python escape hatch
    - For a very interactive app:
        - Django with `django-allauth` pre-authentication (valauble due to admin tools, user standard, and authentication)
        - Single page application (SPA) post-authentication (e.g. React)
        - django-allauth should support building SPA around authentication pages as well, but that has way more implementation time
            - Be careful to still allow tokens to be handle by django-allauth on the server though, otherwise third party scripts will see referrer (security issue)

[explorations-django-allauth]: docs/explorations.md#2-django-allauth


----

TODO: LiveReload setup as part of server
    This is inspiring around maybe building a custom build chain just for LiveReload CLI =o
    https://stackoverflow.com/a/27785960
TODO: Talk through runserver_plus + Werkzeug? + --group dev install pieces?
TODO: Prettier was nice for HTML formatting, does Django have some equivalent?
    djlint has been found =D

TODO: Talk about JWT and difficulty revoking sessions

TODO: Prob use Jinja instead of Django to avoid footguns, https://docs.djangoproject.com/en/4.2/ref/templates/api/#how-invalid-variables-are-handled
https://stackoverflow.com/a/40506337/1960509
https://docs.quantifiedcode.com/python-anti-patterns/django/1.8/migration/template_string_if_invalid_deprecated.html
https://djangosnippets.org/snippets/646/
https://stackoverflow.com/a/15312316/1960509

TODO: Django forms comparison notes
Crispy forms just an HTML DSL
Not saving any time using it
https://django-crispy-forms.readthedocs.io/en/latest/layouts.html

https://www.reddit.com/r/django/comments/20dwgr/do_people_use_django_forms/
Guidance is more or less as expected

--

TODO: Prob a restructure of efficiency of work is in order:
- Django as base layer for loading page with CSRF
- React still handling all routing...?
- But Django being DRF? except for inital page load?
- And React submit via a normal form? (but then React UX prob janky -- e.g. what happens on form error
- This was cascaded because realizing react-create-app (great tooling) also has its own LiveReload
- The modern web is a mess...
- Going to go to sleep...

- This seems promising for LiveReload headaches, https://builtwithdjango.com/blog/set-up-webpack-and-tailwind

TODO: Talk through django-allauth, maybe even use it?
https://django-allauth.readthedocs.io/en/latest/views.html

TODO: AbstractBaseUser exploration, for things like PhoneNumber

TODO: Minus points for HTML pages for nice touches like carrying over email between pages
TODO: Widget for email suggestion

TODO: Bootstrap lacking space-y-* utilities, so handy

TODO: Exploration for Tailwind
TODO: Exploration for React + AJAX

TODO: Real world model example: Create a welcome notification, where user presses X to dismiss (i.e. should have loading state or eager dismiss + restore on fail)

TODO: Talk through a11y tooling from React (Django not nearly as strong)

TODO: How does React hydration work? And what does a setup look like without that?

TODO: Explanation and comparison vs `pip` as well as `venv` and `virtualenvwrapper` coming soon!

TODO: Library comparison for allauth and other options I guess?

TODO: Talk about JSX strengths at expressiveness (e.g. `classnames` with mappings and ternaries), though I think Pug has something similar?

TODO: HTMX author discusses when to not use it - def agree with points from experience -- interactivity is not a fit, https://htmx.org/essays/when-to-use-hypermedia/

TODO: React proxy on Django
TODO: And that boilerplate react-django

TODO: Update the "half of" and "lightly" with quantifiable dates/times

## Stage 0: Minimum Viable Product (MVP) without web app
The goal of a startup is to provide value to others (e.g. time, money, intangibles).

Setting up a web app takes time (e.g. server provisioning, defining models, building pages), and is a barrier to learning lessons quickly.

If I spend 1 month of [Product Design][] (excluding research) and 1 month of build (very aggressive estimates), then launch and nobody wants it -- then that'd be a very frustrating experience.

Instead, use [Product][] techniques to derisk this upfront:

- Conduct interviews ([User Research][])
- Gauge interest through waitlists
- Onboard through Google Forms ([Underdog.io example][])
- Transact over email

[Product Design]: https://www.smashingmagazine.com/2018/01/comprehensive-guide-product-design/#plan-the-structure-of-a-product
[Product]: https://www.productplan.com/learn/what-is-product-management/
[User Research]: https://www.userinterviews.com/ux-research-field-guide-chapter/what-is-user-research
[Figma]: https://www.figma.com/
[Underdog.io example]: https://twolfson.com/2021-06-24-lessons-of-a-startup-engineer#every-decision-is-a-business-decision

> This is not my strong suit. I've only founded once ([Find Work][]) and I'd already convinced myself I was providing value to myself.
>
> I haven't had a chance to test this thoroughly on a product from scratch since then.
>
> In retrospect, I should have taken a broader approach.

If you'd like to learn more, I recommend [Startup School](https://www.startupschool.org/).

[Find Work]: https://github.com/findworkco/app

## Stage 1: Initial build
### Keep on researching
Between [Stage 0](README.md#stage-0-minimum-viable-product-mvp-without-web-app) and building, I recommend continuing to do [User Research][] and leverage mockups/prototypes ([Product Design][]) to derisk the data model.

UIs are hard to get right the first time, and any UI changes can cascade into larger userflow and multi-page code + schema changes.

Assuming I've derisked, and confirmed a web app is the right thing to build (vs a mobile app or no app at all), I'd next consider how interactive this app is going to be.

### Betting on product interactivity
Apps can range in interactivity from being basic [CRUDL][] forms to every page relating to the core product (e.g. music player, maps, photo management).

In my experience, the majority of an app's surface area (and thus development time) comes from basic forms, with 1-2 isolated pages with something that's interactive (e.g. CAD, land selection).

This is important because the development time difference is stark. i.e. A highly interactive app requires building 2 API layers between the server and UI (1 from server for formatting the exposing explicit content values, 1 from UI to read + cache + manage said values).

I estimate this adds 10% development time to every feature. So over a 2-5 year period, that's an additional 2-5 months!

If you're working with a designer, communicate this to avoid accidentally requiring high interactivity. For example:

- Forms within dialogues/modals
- Animations between pages
- Progress bars for forms
- Fields auto-saving after changing

[CRUDL]: https://en.wikipedia.org/wiki/Create,_read,_update_and_delete

To avoid fearmongering app complexity, there's plenty of interactivity which is well-contained in their own components/state:

- Tooltips
- Validation errors
- Progress bars in multi-stage process (e.g. onboarding)
- Dimissable banners
- Toast messages
- Dialogues/modals without forms


For the sake of the rest of our discussion, we'll assume an app with basic forms and 1-2 isolated pages of high interactivity.

If you'd like a version of this repo talking through high interactivity, please [reach out](mailto:todd@twolfson.com) =)

TODO: Provide eval table of different experiences

### Deciding aesthetics
Aesthetics can lead to a significant increase in development time when compounded with other technical decisions.

i.e. If the architectural decision becomes majority HTML forms but with a custom aesthetic, then it's a lot of work because there's no good library to my knowledge with lots of off the shelf components and easy style customizations.

If you're using the architecture is SPA and you use React, then it's less of a drag because there's libraries like [Reakit][] to build around.

My preference for maximizing velocity though is Bootstrap since it provides a design system from the get-go and lots of components.

It doesn't play well with systems like [React][], but with the "basic forms with 1-2 isolated pages of high interactivity", it should work great =)

[Reakit]: https://reakit.io/
[React]: https://react.dev/

TODO: Prob could talk through experiences with all different aesthetics setups

### Architectural decisions
With interactivity (contained) and aesthetics (Bootstrap) decided, we can now start digging into further architectural decisions:

1. [Web Framework: Django](docs/web-framework.md)
2. [Database: PostgreSQL](docs/database.md)
3. [Development Machine: Local computer](docs/development-machine.md)
4. [Development Containment: Language level, nothing else](docs/development-containment.md)

TODO: UI <> Server Interface: Incomplete -- this document needs some rework, doesn't it?

TODO: Authentication (e.g. django-allauth, third party, REST auth, something else)

## Content not covered
There are many many decision I'd like to talk through, but my motivation around this repo has waned (large time sink with uncertain value for others).

As a result, there's a lightning round of content I didn't cover:

- CSS frameworks/UI toolkits (e.g. Bootstrap vs Tailwind vs Inuit.css)
    - Have used these 3 mentioned, as well as no framework
    - Inuit.css was great but not maintained any more =(
    - Bootstrap is best for moving quickly
    - Tailwind is fantastic base layer for designs to create expression on + teams to build on top of
        - Though do need to be careful to contain common patterns and document groups of classes, since maintenance can be tricky otherwise
- CSS preprocessors
    - These are less of a choice one the framework is selected
    - but I do strongly prefer Sass (SCSS flavor) over PostCSS
        - Stylus and LESS are way less prevalent
    - PostCSS always makes me a little nervous that it'll silently stop computing a `calc()` and sending that out, thus breaking a legacy browser
    - It also requires finding/installing every extension rather than giving sane batteries from the start =/
- ES5, ES6, TypeScript, and JavaScript compilation
    - I strongly like when I can copy/paste content from my editor into Dev Tools (i.e. quickly iterate/debug why something isn't working)
    - so I dislike anyhting that's too far from browser-native JS as a result
    - Admittedly, this never happens with JSX (prob since I can TDD around it), only things like logic errors
- Hosting provider selection
    - Landscape and pricing changes too often, do an evaluation table comparison
- Database provider selcetion
    - Landscape and pricing changes too often, do an evaluation table comparison
- Documenting in-repo vs outside of repo
    - I'd been team "in-repo" for years,
    - but recently switched to "outside of repo" since it allows for easier multi-repo onboarding
    - and historical docs for historical code isn't necessary when always running `latest`
    - Caveat: In-repo + monorepo is preferred if this is an open source product (for easy documentation versioning)
    - If you **need** in-repo, then Markdown is preferred
        - reStructuredText is finnicky around headings
        - Plain text lacks hierarchy when being served
        - Not sure about others
    - If this is an open source product though, then
- Monorepo vs not
    - I've never worked on a true monorepo, but would be on the fence since it requires additional tooling
- Monolith vs not
    - Monolith is easier because all the code is colocated
    - and it simplifies pull requests
    - as well as deployments
- Releases + versioning
    - Release on every PR is preferred
    - Versioning was something I used to do, but have since realized there's little value despite a decent amount of effort (e.g. `git tag` + `git push` in deploys)
    - Caveat: Definitely do if the product is open source
- Squashed commits vs not
    - I strongly prefer squashed commits from every PR
        - (despite evidence otherwise on my open source repos)
    - It allows for sane reverting if a firefighting scenario happens
- Version Control System and hosting
    - I've used SVN a long time ago, and Git otherwise
    - Git isn't the most intuitive but if you learn the fundamentals (e.g. <https://git-scm.com/book/en/v2>)
    - then it becomes much easier to keep track of what's going on
    - GitHub is my preference for hosting
    - I have no experience with Gitlab, Bitbucket, or Sourcehut
    - There was a brief period where I used Phabricator, but the setup seemed very involved
- Secret management (e.g. hardcode vs env variables vs .env vs SOPS vs others)
    - Either hardcode or environment variables with `.env` for local development
    - Hardcode is surprisingly prevalent in early stage industry
    - and there's not a whole lot extra security compromise to be concerned about
    - but the more "defense in depth" version is definitely environment variables
    - SOPS is excessive (and tricky with a small team) since versioning doesn't matter when always shipping `latest`

Additionally, there's pieces I wanted go cover around how the product and business continues to grow, and the setup is primed for that:

- Continuous Integration
    - Strongly preferred since it adds velocity. Testing and linting ftw
- Continuous Deployment
    - A bit tedious to set up, and I find little extra value vs having a one-click deploy after landing a PR
- Testing (integration, unit, visual)
    - Unit testing definitely
    - Visual is only good for one-shot large scale CSS rework, otherwise it's a PITA to keep up to date
    - Integration can be good but it's also quite brittle + adds little value
        - Manual testing (which should always be done on release as-is) takes care of this generally
- Linting and programming style
    - ESLint and prettier do a fantastic job of ensuring common formatting and no accidental errors being introduced, definitely use these if you can
- Development Tools (e.g. Stellar)
    - Stellar is wonderful for snapshotting the DB to iterate on for a feature, then going back to `main` without hiccups
- History and auditing
    - django-simple-history is fantastic for getting auditable history (e.g. who/what) without getting too much in the way =D
    - There is some elbow grease needed to enforce the convention, but it pays dividends in its investment
- Admin tooling
    - Django Admin provides amazing infrastructure, don't leave home without it =D
- Sentry and error monitoring
    - Another piece of infrastructure that pays amazing dividends
    - Get notified of bugs that your server and users are encountering, what a great concept! =D
- Server stats monitoring
    - It's good to have but not critical
    - Prob can defer until you start to notice large scaling

Weird thoughts and tangents:
- React hydrating Django rendered content
    - Just say no, you're doubling up on the generated code (requiring React to stay consisting with Django)
    - and there's been chatter around hydration not being great
    - and definitely costs an innovation token

## Context
I decided to leave NCX at the end of May 2023.

I had some lingering architectural questions (outside of NCX, but full-time focused) that I feel would best be solved through exploration.

The last time I publicly documented my architectural preferences was through open sourcing Find Work in December 2019.

And as expected in hindsight, these have aged in a mixed manner (not bad but not great either).

- https://github.com/findworkco/app
- https://github.com/findworkco/scripts

I've also found this repo useful in discussion with various startups, hence the "good enough" completion in October 2023.

## Documentation format
You may have noticed the HTML tables in some of our Markdown `docs/` files.

This is due to needing multi-line support in tables, but Markdown not supporting that.

We tried reStructuredText but that fell short as well (e.g. no [easy support for hyperlinks in bold text](https://docutils.sourceforge.io/FAQ.html#is-nested-inline-markup-possible), also annoyingly brittle when writing))

As a result, HTML tables felt like the best compromise for readability in Markdown content.

In an ideal world, we'd prob be using a WYSIWYG for such content.

## Unlicense
As of May 11 2023, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the [UNLICENSE][].

[UNLICENSE]: UNLICENSE
