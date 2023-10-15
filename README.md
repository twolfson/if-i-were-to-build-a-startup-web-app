# If I Were to Build a Startup Web App

# THIS IS A WORK IN PROGRESS, PLEASE IGNORE THE MESS

- TODO: See TODOs

Choices, explanations, and documentation around if I were to build a startup web app

The goal is to build a product as quickly and efficiently as possible.

This was mostly written in May and October 2023. For exceptions, there will be a note.

- TODO: Fill in tl;dr with more info as we decide on things
- TODO: Have this act as a table of contents
- TODO: For each of these items, ensure we talk about things we're also sidestepping with our given choice (e.g. Django + batteries included)

1. First, [Minimum Viable Product (MVP) without web app](README.md#stage-0-minimum-viable-product-mvp-without-web-app)
2. Then, [Betting on product interactivity, deciding aesthetics (TODO), and assuming isolated high interactivity for discussion](README.md#stage-1-initial-build)
3. Then, making architectural decisions:
    1. [Web framework: Django](docs/web-framework.md)
        - For a highly interactive setup, Django is still invaluable due to its admin tooling, user standard, and authentication
    2. [Database: PostgreSQL](docs/database.md)
    3. [Development Machine: Local computer](docs/development-machine.md)
    4. [Development Containment: Language level, nothing else](docs/development-containment.md)
    5. UI <> Server Interface: Incomplete
        - Rough recommendation: Django with Bootstrap + limited custom JS
            - For a very interactive app, then I recommend django-allauth HTML forms pre-authentication and single page application (SPA) post-authentication
            - django-allauth should support building SPA around authentication pages as well, but we're prioritizing building a product
            - TODO: Talk about how we're prioritizing minimizing shipping time at start of content
        - Why this is a rough recommendation:
            - I've used plenty of frameworks with just GET/POST responses and limited JS
            - However, I've never used Django with it
            - so I'd like to do a sanity check exploration with that final sign-off
            - TODO: Broader Python templating evaluation/comparison?
                - Mako seems like a winner due to having bare Python escape hatch
    6. Styling Framework/System:
        - TODO: Explain TBD
        - TODO: CSS preprocessor or postcompiler
        - [Work in progress document](docs/styling-framework-system.md)
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

### Architectural decisions
With interactivity decided, we can now start digging into architectural decisions:

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

TODO: Pull into other content
"""
2023-05-14:
Architecture where JSX is renderer in Django
And page load hydration is select regions

Benefit would be no serializer busy work

But unclear how that'd side step deeper lookups
But maybe it's just like a really fancy form

Also definitely an innovation token

This also isn't much different from rendering HTML with context as JSON

Main concern of react in a per page setup
Is seeing a loading spinner so damn often
(prob need to use throttling as a demo)
--
Django auth pages drawback
Can't do email suggest
Can't use common validation styles
"""

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

TODO: Auth validation is bad idea with react because scrubbing out of hand. HTTP referrer too late


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
