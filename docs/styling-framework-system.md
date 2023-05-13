# Database Analysis
## Decision
TODO: Capture decision

## Description
User Interfaces (UIs) need styling outside of what HTML provides by default (regardless of [UI <> Server Interface](ui-server-interface.md)).

There's 2 common setups for handling this but the term "CSS framework" often conflates them. I'll be distinguishing them as follows:

- UI toolkit (e.g. [Bootstrap][], [Foundation][] - Provides opinionated styles and components for usage within application
- CSS framework (e.g. [Inuit.css][], [Reakit][], [Tailwind][]) -

[Bootstrap]: https://getbootstrap.com/
[Foundation]: https://get.foundation/
[Inuit.css]: https://github.com/inuitcss/inuitcss/tree/6.0.0
[Reakit]: https://reakit.io/
[Tailwind]: https://tailwindcss.com/

TODO: Technically Reakit is only for building components, not styling. And Bootstrap doubles as component library. Maybe we should rephrase this as "component system" or "component framework" or "UI framework"?

## Comparison
|                                     Name                                    | Non-trivial previous experience? |                                                            Description                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HTML forms, no AJAX                                                         | ✔️ (25-50% of career)            | Operate with browser built-in form submission, e.g. `<form>` and `<input>`                                                         | [MDN article](https://developer.mozilla.org/en-US/docs/Learn/Forms/Your_first_form). Works quite well and has good associated UX (progress shown in address bar). Extension for improved UX (e.g. loading spinners)<br/><br/>Major strength is no need to track DB state from browser locally as well as easy to build + maintain functionality like links that perform logic and redirects as needed<br/><br/>Major downside reduced code reuse for [Single-Page Applications (SPA)](https://developer.mozilla.org/en-US/docs/Glossary/SPA), but in my experience these are quite rare and not the primary purpose of a web app                                                                                                                                                                                                                                                                                                      |

