# UI Framework Analysis
## Decision
TODO: Capture decision

## Description
User Interfaces (UIs) need styling outside of what HTML provides by default (regardless of [UI <> Server Interface](ui-server-interface.md)). This also may encapsulate interactivity, so I'm expanding this broadly as "UI frameworks".

The term "CSS framework" can conflate the interactivity piece, so I'll be addressing these in 3 comparisons.

The end solution must support both styling as well as interactivity, but this can be a combination.

Before we can talk about that though, we should also talk about CSS compilation.

## CSS Compilation Comparison
|     Name     | Non-trivial previous experience? | Description | Notes |
|--------------|----------------------------------|-------------|-------|
| No framework | ✔️ (??% of career)               |             |       |
| Sass         | ✔️ (??% of career)               |             |       |
| Stylus       | ✔️ (??% of career)               |             |       |
| LESS         | ✔️ (??% of career)               |             |       |
| PostCSS      | ✔️ (??% of career)               |             |       |

TODO: SUIT CSS

TODO: Mentions about OOCSS, SMACSS, and BEM

TODO: Mentions about selector precedence

TODO: Web components, Backbone, Angular, Ember, Vue, etc

## Styling Only Framework Comparison
|      Name     | Non-trivial previous experience? |              Description               | Notes |
|---------------|----------------------------------|----------------------------------------|-------|
| No framework  | ✔️ (??% of career)               | Build your own CSS system from scratch |       |
| [Bourbon][]   |                                  |                                        |       |
| [Inuit.css][] |                                  |                                        |       |
| [Tailwind][]  |                                  |                                        |       |

## Component Only Framework Comparison
|     Name     | Non-trivial previous experience? | Description | Notes |
|--------------|----------------------------------|-------------|-------|
| No framework | ✔️ (??% of career)               |             |       |
| [Reakit][]   |                                  |             |       |
| [React][]    |                                  |             |       |

## Styling + Component Framework Comparison
|      Name      | Non-trivial previous experience? | Description | Notes |
|----------------|----------------------------------|-------------|-------|
| No framework   | ✔️ (??% of career)               |             |       |
| [Bootstrap][]  |                                  |             |       |
| [Foundation][] |                                  |             |       |



----

There's 2 common setups for handling this but the term "CSS framework" often conflates them. I'll be distinguishing them as follows:

- UI toolkit (e.g. [Bootstrap][], [Foundation][] - Provides opinionated styles and components for usage within application
- CSS framework (e.g. [Inuit.css][], [Reakit][], [Tailwind][]) - Provides foundation to build your own styles and components from

[Bootstrap]: https://getbootstrap.com/
[Foundation]: https://get.foundation/
[Inuit.css]: https://github.com/inuitcss/inuitcss/tree/6.0.0
[Reakit]: https://reakit.io/
[Tailwind]: https://tailwindcss.com/

TODO: Technically Reakit is only for building components, not styling. And Bootstrap doubles as component library. Maybe we should rephrase this as "component system" or "component framework" or "UI framework"?

TODO: jQuery, YUI, MooTools, React
