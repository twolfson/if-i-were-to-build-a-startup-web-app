UI <> Server Interface Analysis
===============================

.. Raw HTML support due to rST not supporting inline formatting + links, https://docutils.sourceforge.io/FAQ.html#is-nested-inline-markup-possible
   There's also | syntax, but that is tricky for editing with tables, so using :raw-html:, https://stackoverflow.com/a/51199504/1960509

.. role:: raw-html(raw)

    :format: html

This comparison doesn't quite line up with any early decisions being made (i.e. interactivity drives this, not technical needs).

But it does give context to broader implications technically.

Regardless, here's my preferences:

**Winner: HTML forms, limited AJAX**

**Runner-up: No HTML forms, AJAX only**

Explanations in comparison below

Description
-----------
A web app inherently has a client (aka browser aka UI) and server split. There is data passed from one to another, and the choice of how we should present that as an interface.

There's various framings like `fat client and thin client <https://www.parallels.com/tips/thin-clients/vs-thick/>`_, but I think this removes focus from the development experience and overweights severity to user experience (UX)

Comparison
----------
+-----------------------+-----------------------+---------------------------+-----------------------------------------------------------------------------+
| Name                  | Non-trivial           | Description               | Notes                                                                       |
|                       | previous experience?  |                           |                                                                             |
+=======================+=======================+===========================+=============================================================================+
| HTML forms, no AJAX   | ✔️ (25-50% of career) | Operate with browser      | `MDN article <MDN forms_>`_.                                                |
|                       |                       | built-in form submission, | Works quite well and has good associated UX                                 |
|                       |                       | e.g. ``<form>``           | (progress shown in address bar).                                            |
|                       |                       | and ``<input>``           | Extension for improved UX (e.g. loading spinners)                           |
|                       |                       |                           |                                                                             |
|                       |                       |                           | Major strength is no need to track DB state                                 |
|                       |                       |                           | from browser locally as well as                                             |
|                       |                       |                           | easy to build + maintain functionality like                                 |
|                       |                       |                           | links that perform logic and redirects as needed                            |
|                       |                       |                           |                                                                             |
|                       |                       |                           |                                                                             |
|                       |                       |                           | Major downside reduced code reuse for                                       |
|                       |                       |                           | `Single-Page Applications (SPA) <MDN SPA_>`_,                               |
|                       |                       |                           | but in my experience these are quite rare                                   |
|                       |                       |                           | and not the primary purpose of a web app                                    |
+-----------------------+-----------------------+---------------------------+-----------------------------------------------------------------------------+
| :raw-html:`<strong>`  | ✔️ (10% of career)    | Use ``<form>`` and        | Same as "HTML forms, no AJAX" but a little more lenient.                    |
| HTML forms,           |                       | such majority of time,    | e.g. We don't want UX to suffer for things                                  |
| limited AJAX          |                       | but exit in               | like dismissing notifications,                                              |
| (winner)              |                       | occasional scenarios like | so support those as a one-off                                               |
| :raw-html:`</strong>` |                       | secondary form actions    |                                                                             |
|                       |                       | (e.g. notification        |                                                                             |
|                       |                       | dismissal)                | This was frustrating to deal with in early web days                         |
|                       |                       |                           | with jQuery due to page specific focus,                                     |
|                       |                       |                           | but I think as long as widget-focused approach is used                      |
|                       |                       |                           | (e.g. `Bootstrap`_, `"islands" architecture`_),                             |
|                       |                       |                           | then it should generally be maintainable and great UX                       |
|                       |                       |                           |                                                                             |
|                       |                       |                           |                                                                             |
|                       |                       |                           | Sometimes people might get thrown for things like                           |
|                       |                       |                           | "How do I build an interactive map around with this?"                       |
|                       |                       |                           | :raw-html:`<br/>`                                                           |
|                       |                       |                           | In that scenario, I'd make that specific page React-based                   |
|                       |                       |                           | and build the UI around it,                                                 |
|                       |                       |                           | but the React would update HTML form content and                            |
|                       |                       |                           | the submission would happen without obscuring it.                           |
|                       |                       |                           | :raw-html:`<br/>`                                                           |
|                       |                       |                           | Or maybe the page is well-contained to self-contain AJAX,                   |
|                       |                       |                           | as long as it's to 1-2 endpoints at most                                    |
+-----------------------+-----------------------+---------------------------+-----------------------------------------------------------------------------+
| HTML forms with       | ✔️ (10% of career)    | Swap content from an      | I rolled our own setup for this in 2013                                     |
| server-driven         |                       | HTTP response with        | for https://riders.uber.com/ and deeply regret it.                          |
| HTML updates          |                       | a declared target         | :raw-html:`<br/>`                                                           |
| (e.g. `HTMX`_)        |                       |                           | It was a good idea on paper (had buy-in from others),                       |
|                       |                       |                           | but in practice it made for awful UX (e.g. no good loading spinners)        |
|                       |                       |                           | and content swaps felt unexpected.                                          |
|                       |                       |                           | :raw-html:`<br/>`                                                           |
|                       |                       |                           | Additionally, the actual code seemed fragmented/confusing                   |
|                       |                       |                           | because updates were split across 2 places                                  |
|                       |                       |                           | (server saying what to update to, browser saying how to swap).              |
|                       |                       |                           | :raw-html:`<br/>`                                                           |
|                       |                       |                           | Comically, the `HTMX author agrees on similar points <HTML when to use_>`_. |
|                       |                       |                           | :raw-html:`<br/>`                                                           |
|                       |                       |                           | I strongly advise against this approach                                     |
+-----------------------+-----------------------+---------------------------+-----------------------------------------------------------------------------+
| HTML forms            |                       | Leverage Django           | Seems like it'd provide a good UX,                                          |
| pre-login,            |                       | built-in support          | but I believe it'd destroy developer experience (DX)                        |
| AJAX only             |                       | for auth pages            | by needing to remember 1 set of rules for some pages,                       |
| forms/content         |                       | and cookie sessions       | and a different set for another.                                            |
| after login           |                       | to start,                 | :raw-html:`<br/>`                                                           |
|                       |                       | but then                  | Not to mention double tooling for things like linting                       |
|                       |                       | lean into AJAX only       | (e.g. HTML errors) as well as reduced code reusability.                     |
|                       |                       | afterwards                | :raw-html:`<br/>`                                                           |
|                       |                       |                           | Additionally, you still run into the drawbacks of                           |
|                       |                       |                           | "No HTML forms, AJAX only" like cache management.                           |
|                       |                       |                           |                                                                             |
|                       |                       |                           |                                                                             |
|                       |                       |                           | EDIT: I'm later eating my words here                                        |
|                       |                       |                           | (though only in the high interactivity context),                            |
|                       |                       |                           | because this is exactly what I'm recommending =/                            |
|                       |                       |                           | :raw-html:`<br/>`                                                           |
|                       |                       |                           | It's prob good to hit the ground running,                                   |
|                       |                       |                           | but may lead to confusion long-term.                                        |
|                       |                       |                           | :raw-html:`<br/>`                                                           |
|                       |                       |                           | But it's kind of hard to run into issues in                                 |
|                       |                       |                           | the ``django-allauth`` case since HTML forms                                |
|                       |                       |                           | are not controlled by us                                                    |
|                       |                       |                           | :raw-html:`<br/>`                                                           |
|                       |                       |                           | whereas the React ones would be                                             |
+-----------------------+-----------------------+---------------------------+-----------------------------------------------------------------------------+
| No HTML forms,        | ✔️ (20% of career)    | Control everything        | Works fantastic for things like UI management                               |
| AJAX only             |                       | through a SPA,            | and dynamically shifting through pages (UX),                                |
|                       |                       | from authentication       | but extremely frustrating when it comes to                                  |
|                       |                       | to page navigation        | DB state tracking (DX).                                                     |
|                       |                       |                           |                                                                             |
|                       |                       |                           |                                                                             |
|                       |                       |                           | i.e. For this to work, the SPA needs to                                     |
|                       |                       |                           | effectively have a copy of the API responses,                               |
|                       |                       |                           | and know when 1 save requires                                               |
|                       |                       |                           | breaking the cache of other existing responses.                             |
|                       |                       |                           |                                                                             |
|                       |                       |                           |                                                                             |
|                       |                       |                           | This leads to a lot of busy work with little value,                         |
|                       |                       |                           | that could have been avoided with another architecture.                     |
|                       |                       |                           | :raw-html:`<br/>`                                                           |
|                       |                       |                           | Additionally, you probably lose a lot of                                    |
|                       |                       |                           | freebies we got from the web framework selection                            |
|                       |                       |                           | (e.g. rebuilding login + sign up + forgot password + sessions).             |
|                       |                       |                           | :raw-html:`<br/>`                                                           |
|                       |                       |                           | Also, if done incorrectly (e.g. not using cookie sessions),                 |
|                       |                       |                           | then it also introduces security issues around                              |
|                       |                       |                           | HTTP referrers being sent to third party scripts                            |
|                       |                       |                           | and JWT tokens being unable to be invalidated.                              |
+-----------------------+-----------------------+---------------------------+-----------------------------------------------------------------------------+

.. _`MDN forms`: https://developer.mozilla.org/en-US/docs/Learn/Forms/Your_first_form
.. _`MDN SPA`: https://developer.mozilla.org/en-US/docs/Glossary/SPA
.. _`Bootstrap`: https://getbootstrap.com/
.. _`"islands" architecture`: https://www.patterns.dev/posts/islands-architecture
.. _`HTMX`: https://htmx.org/
.. _`HTML when to use`: https://htmx.org/essays/when-to-use-hypermedia/
