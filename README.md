# If I Were to Build a Startup Web App
- TODO: Snazzy graphic
- TODO: See TODOs

Choices, explanations, and documentation around if I were to build a startup web app

Unless stated or seen otherwise, this was all written in roughly May 2023

- TODO: Fill in tl;dr with more info as we decide on things
- TODO: Have this act as a table of contents
- TODO: For each of these items, ensure we talk about things we're also sidestepping with our given choice (e.g. Django + batteries included)

1. First, Minimum Viable Product (MVP) without web app
2. Then:
    1. Web framework: Django
        - TODO: Talk through languages
        - TODO: Talk through serverless options
    2. Docker: No
    - PostgreSQL
    - React, but not for HTTP
        - TODO: Talk through how if not using Django built-ins
    - Bootstrap?? Tailwind??
    - Runbook as documentation
    - Hosting provider selection
    - Documenting in-repo vs outside of repo
    - Monorepo vs not
    - Monolith vs not
    - Virtual environments
    - Scripting (deployments, commands)
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

Assuming you've derisked though, let's get into tactical decisions:

1. [Web Framework: Django](docs/web-framework.md)

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

----

TODO:
What a product example is
Not covering mobile focused API

Firebase setups

Take everything with grain of salt
Especially with age

These are strictly starting points for discussions. No eng decision ever made in isolation. Impacts me and future team mates. Decisions rarely get revisited after implemented unless repeat work blocks. So friction cost present but never paid. Boiling the frog metaphorically

TODO: Secret management (hardcode vs env variables vs .env vs SOPS vs more) + interplay with Docker

TODO:
Rails does have generate utility but can't recall last time I wanted that. Copy paste as convention is best pit of success

Secondary to this would be a runbook as its an operational process. Link to article


## Context
NCX and I have decided to part ways. This will likely finalize at the end of May 2023.

I've had some lingering architectural questions that I feel would best be solved through exploration.

Additionally, the last time I publicly documented my architectural preferences and setup was through open sourcing Find Work in December 2019.

And as expected in hindsight, these have aged alright -- not bad but not great either.

- https://github.com/findworkco/app
- https://github.com/findworkco/scripts

## Unlicense
As of May 11 2023, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the [UNLICENSE][].

[UNLICENSE]: UNLICENSE
