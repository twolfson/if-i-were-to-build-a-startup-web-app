# If I Were to Build a Startup Web App

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
    - Why this is a rough recommendation:
        - I've used plenty of frameworks with just GET/POST responses and limited JS
        - However, I've never used Django as an HTML form app (was REST API + admin tools) nor django-allauth in a non-trivial manner
            - In our [Explorations document][explorations-django-allauth], we found Django without django-allauth was quite infuriating for self-serve signups
        - so take this advice with a grain of salt
        - There's [addititional notes for building a fuller example at the bottom](#if-we-were-to-build-a-fuller-example)
    - For a very interactive app:
        - Django with `django-allauth` pre-authentication (valauble due to admin tools, user standard, and authentication)
        - Single page application (SPA) post-authentication (e.g. React)
        - `django-allauth` should support building SPA around authentication pages as well, but that has way more implementation time
            - Be careful to still allow password reset tokens/similar to be handle by `django-allauth` on the server though, otherwise third party scripts will see referrer (security issue)
        - [Working example of this](explorations/4-django-allauth-react-proxy)

[explorations-django-allauth]: docs/explorations.md#2-django-allauth

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

### Deciding aesthetics
Aesthetics can lead to a significant increase in development time when compounded with other technical decisions.

i.e. If the architectural decision becomes majority HTML forms but with a custom aesthetic, then it's a lot of work because there's no good library to my knowledge with lots of off the shelf components and easy style customizations.

If you're using the architecture is SPA and you use React, then it's less of a drag because there's libraries like [Reakit][] to build around.

My preference for maximizing velocity though is Bootstrap since it provides a design system from the get-go and lots of components.

It doesn't play well with systems like [React][], but with the "basic forms with 1-2 isolated pages of high interactivity", it should work great =)

[Reakit]: https://reakit.io/
[React]: https://react.dev/

### Architectural decisions
With interactivity (contained) and aesthetics (Bootstrap) decided, we can now start digging into further architectural decisions:

- [Web Framework: Django](docs/web-framework.rst)
- [Database: PostgreSQL](docs/database.rst)
- [Development Machine: Local computer](docs/development-machine.rst)
- [Development Containment: Language level, nothing else](docs/development-containment.rst)
- [UI <> Server Interface](docs/ui-server-interface.rst)

There's also various explorations/discussions as well:
- [Explorations](docs/explorations.md)
- [Django <> React Security and Architecture](docs/django-react-security-and-architecture.md)

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
- Database provider selection
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
- accessibility (a11y) of normal templates vs React
    - React has super powerful a11y tooling, which other templating systems lack
    - I don't think it's a reason to prioritize shifting your whole world view around it
    - but it's a major detail, esp if you plan on having juniors who aren't used to a11y
- Authentication (e.g. django-allauth, third party (e.g. Auth0, AWS Cognito), REST auth, something else)
    - django-allauth is ideal because it keeps users in the DB (vs third party)
    - and it sticks to cookie sessions (vs REST auth) and is one less library
    - and it has so many login providers to integrate easily =D
    - Keeping users in DB is ideal for admin tools and business intelligence
        - i.e. Separate systems adds tax on people supporting customers to jump between systems

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
    - [LiveReload CLI][] is very powerful for updating HTML and CSS after you modify it, without that pesky mouse move + click (adds up a lot)
    - `runserver_plus` in Django extensions is very handy for `--print-sql` and such
    - Poetry is wonderful for tracking dependency versions
- History and auditing
        - I could also talk about virtualenvwrapper being great, but Poetry removes the need for that =)
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

[LiveReload CLI]: https://github.com/lepture/python-livereload

One-off time consuming info like:
- Clarifying what "half of my career" and "lightly" mean in terms of years
- Providing eval table with years for newer content like product interactivity and aesthetics systems

### Things I wanted to dig into/explore more
- Alternative CSS frameworks like Bourbon or SuitCSS
    - Bootstrap is generally good but lacks the full breadth of Tailwind (e.g. `space-y-*`)

### If we were to build a fuller example
- Explore Mako as templating language
    - Django had footguns which we strongly disliked
        - https://docs.djangoproject.com/en/4.2/ref/templates/api/#how-invalid-variables-are-handled
        - https://stackoverflow.com/a/40506337/1960509
        - https://docs.quantifiedcode.com/python-anti-patterns/django/1.8/migration/template_string_if_invalid_deprecated.html
        - https://djangosnippets.org/snippets/646/
        - https://stackoverflow.com/a/15312316/1960509
    - Mako has a Python escape (which Django doesn't, leading to development frustration)
    - Jinja2 might also resolve these concerns
    - Template language comparison: https://gist.github.com/twolfson/b861c182107cefcef086266c3b4b83a6
- Explore using AbstractBaseUser more (e.g. PhoneNumber) since we lacked experience on that
- Building custom JS widget for something like email suggestion
- Real world model example: Create a welcome banner, where user presses "&times;" to dismiss (i.e. should have loading state or eager dismiss + restore on fail)

## Context
I decided to leave NCX at the end of May 2023.

I had some lingering architectural questions (outside of NCX, but full-time focused) that I feel would best be solved through exploration.

The last time I publicly documented my architectural preferences was through open sourcing Find Work in December 2019.

And as expected in hindsight, these have aged in a mixed manner (not bad but not great either).

- https://github.com/findworkco/app
- https://github.com/findworkco/scripts

I've also found this repo useful in discussion with various startups, hence the "good enough" completion in October 2023.

## Documentation format
You may have noticed the some of the files in `docs/` are reStructuredText, instead of Markdown.

This is due to needing multi-line support in tables, but Markdown not supporting that.

For editing tables sanely, we use Sublime Text with the [Table Editor][] plugin:

- Set "Table Editor: Enable for current view"
- Set "Table Editor: Set Table Syntax for reStructuredText"
- Set "Table Editor: Disable detect_header for current view"
- Set "Table Editor: Disable keep_space_left for current view"

For previewing output as you build (since reStructuredText is brittle) and reStructuredText preview support isn't great, I suggest:

- Using a file watcher (e.g. `listen-spawn`, `entr`). For example:
    - `bash -c rst2html.py docs/database.rst > tmp.html`
- Starting an HTTP server. For example:
    - `serve .`
- Enabling LiveReload CLI with a delay:
    - `livereload --wait 0.3`
- Opening our `tmp.html` file in our browser and letting it refresh as we write

[Table Editor]: https://packagecontrol.io/packages/Table%20Editor

Some Markdown &lt;&gt; reStructuredText footguns:

- Bullets require 2 spaces only and line break after each one
- Headings don't correlate to h1, h2, etc but instead decrease in intensity from the highest one present
- Double ticks (\`\`) are required to make a &lt;code&gt; element

## Unlicense
As of May 11 2023, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the [UNLICENSE][].

[UNLICENSE]: UNLICENSE
