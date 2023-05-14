# If I Were to Build a Startup Web App
- TODO: Snazzy graphic
- TODO: See TODOs

Choices, explanations, and documentation around if I were to build a startup web app

Unless stated or seen otherwise, this was all written in May 2023

- TODO: Fill in tl;dr with more info as we decide on things
- TODO: Have this act as a table of contents
- TODO: For each of these items, ensure we talk about things we're also sidestepping with our given choice (e.g. Django + batteries included)

1. First, [Minimum Viable Product (MVP) without web app](README.md##stage-0-minimum-viable-product-mvp-without-web-app)
2. Then:
    1. [Web framework: Django](docs/web-framework.md)
    2. [Database: PostgreSQL](docs/database.md)
    3. [Development Machine: Local computer](docs/development-machine.md)
    4. [Development Containment: Language level, nothing else](docs/development-containment.md)
    5. [UI <> Server Interface: HTML forms, limited AJAX](docs/ui-server-interface.md)
        - TODO: Show an example with notification dismissal on same page
        - TODO: Show an example with model opens and dismissals (Bootstrap strongsuit)
        - TODO: Compute actual years for each
    6. [Styling Framework/System: TBD](docs/styling-framework-system.md)
        - TODO: Explain TBD
        - TODO: CSS preprocessor or postcompiler
    - Bootstrap?? Tailwind??
    - ES5?? ES6?? Compilation??
        - Prob concat + minify at a... minimum ;D I wonder if Parcel works as a freebie
    - Repeatability: Runbook as documentation
    - Hosting provider selection
    - Database provider selection
    - Documenting in-repo vs outside of repo
    - Monorepo vs not
    - Monolith vs not
    - Virtual environments
    - Scripting (deployments, commands) -- bash vs Python, when and where and why
3. Areas of Growth
    - Continuous Integration
    - Continuous Deployment
    - Testing (integration, unit, visual)
    - Linting and programming style
    - Development Tools (e.g. Stellar)
    - History and auditing
    - Admin tooling

TODO: Talk through innovation tokens?
TODO: Talk through "cost savings" vs "time savings"
TODO: Talk through "code maintenance as fact"
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

## Introduction
I'm a startup engineer. 3x first engineer, former Uber engineer, and have 12 years experience at these and more startups.

I've provided [more context at the bottom](README.md#context) of this README, but that's not why you're here.

Let's dig in.

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

> This is not my strong suit as with [Find Work][], I'd already convinced myself I was providing value to myself.
>
> And I haven't had a chance to test this thoroughly on a product from scratch since then.
>
> However, in retrospect, I should have taken a broader approach.

If you'd like to learn more, I recommend [Startup School](https://www.startupschool.org/).

[Find Work]: https://github.com/findworkco/app

## Stage 1: Initial build
Between [Stage 0] and building, I recommend continuing to do [User Research][] and leverage mockups/prototypes ([Product Design][]) to derisk the data model.

UIs are hard to get right the first time, and any UI changes can cascade into larger userflow and multi-page code + schema changes.

Assuming I've derisked, and confirmed a web app is the right thing to build (vs a mobile app or no app at all), here are the tactical decisions I'd make:

1. [Web Framework: Django](docs/web-framework.md)
2. [Database: PostgreSQL](docs/database.md)

<!-- TODO: Keep this up to date with list as top -->

## Low-level decisions
### Documentation
TODO: Markdown vs reStructured Text vs plain text vs external (Slab, Notion, etc) something else

### Releases
TODO: Releases + versioning

### Squashed commits vs not
TODO: Explain this

### Version Control System and hosting
TODO: Explain this

### Why are comparisons tables vs lists or something else?
TODO: Explain this


TODO: Talk about Sentry and error monitoring
TODO: Talk about server stats monitoring

----

TODO:
What a product example is
Not covering mobile focused API (e.g. Firebase, Supabase)

Firebase setups

Take everything with grain of salt
Especially with age

These are strictly starting points for discussions. No eng decision ever made in isolation. Impacts me and future team mates. Decisions rarely get revisited after implemented unless repeat work blocks. So friction cost present but never paid. Boiling the frog metaphorically

TODO: Secret management (hardcode vs env variables vs .env vs SOPS vs more) + interplay with Docker

TODO:
Rails does have generate utility but can't recall last time I wanted that. Copy paste as convention is best pit of success

Secondary to this would be a runbook as its an operational process. Link to article


## Context
I've decided to leave NCX at the end of May 2023.

I've had some lingering architectural questions (outside of NCX, but full-time focused) that I feel would best be solved through exploration.

The last time I publicly documented my architectural preferences was through open sourcing Find Work in December 2019.

And as expected in hindsight, these have aged in a mixed manner (not bad but not great either).

- https://github.com/findworkco/app
- https://github.com/findworkco/scripts

## Unlicense
As of May 11 2023, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the [UNLICENSE][].

[UNLICENSE]: UNLICENSE
