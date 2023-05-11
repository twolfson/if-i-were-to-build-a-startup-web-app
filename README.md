# If I Were to Build a Startup Web App
TODO: Snazzy graphic
TODO: See TODOs

Choices, explanations, and documentation around if I were to build a startup web app

Unless stated or seen otherwise, this was all written in roughly May 2023

TODO: Fill in tl;dr with more info as we decide on things
TODO: Have this act as a table of contents

1. First, MVP without web app
2. Then:
    - No Docker
    - Django
        - TODO: Talk through languages
        - TODO: Talk through serverless options
    - PostgreSQL
    - Bootstrap?? Tailwind??
    - React but not for HTTP
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

TODO: Talk through innovation tokens?
TODO: Talk through "cost savings" vs "time savings"
TODO: Talk through "code maintenance as fact"

## Introduction
I'm a startup engineer. 3x first engineer, former Uber engineer, and have worked at many more startups.

I've provided [more context at the bottom](README.md#context) of this README, but that's not why you're here.

Let's dig in.

## Stage 0: MVP without web app
The goal of a startup is to provide value to others (e.g. time, money, intangibles).

Setting up a web app takes time (e.g. server provisioning, defining models, setting up layout), and is a barrier to learning lessons quickly.

If I spend 1 month of Product Design and 1 month of build (very aggressive estimates), then launch and nobody wants it -- then that'd be a very frustrating experience.

Instead, use [Product][] techniques to derisk this upfront:

- Conduct interviews ([User Research][])
- Build prototypes
- Build waitlists

[User Research]: https://www.userinterviews.com/ux-research-field-guide-chapter/what-is-user-research

[Product]: https://www.productplan.com/learn/what-is-product-management/

> This is not my strong suit as with [Find Work][], I'd already convinced myself I was providing value to myself.
>
> And I haven't had a chance to test this thoroughly on a product from scratch since then.
>
> However, in retrospect, I should have taken a broader approach.

If you'd like to learn more, I recommend [Startup School](https://www.startupschool.org/).

[Find Work]: https://github.com/findworkco/app

## Low-level decisions
### Documentation
TODO: Markdown vs reStructured Text vs plain text vs external (Slab, Notion, etc) something else

### Releases
TODO: Releases + versioning

### Squashed commits vs not
TODO: Explain this

### Version Control System and hosting
TODO: Explain this

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
