# UI <> Server Interface Analysis

This comparison doesn't quite line up with any early decisions being made (i.e. interactivity drives this, not technical needs).

But it does give context to broader implications technically.

Regardless, here's my preferences:

**Winner: HTML forms, limited AJAX**

**Runner-up: No HTML forms, AJAX only**

Explanations in comparison below

## Description
A web app inherently has a client (aka browser aka UI) and server split. There is data passed from one to another, and the choice of how we should present that as an interface.

There's various framings like [fat client and thin client](https://www.parallels.com/tips/thin-clients/vs-thick/), but I think this removes focus from the development experience and overweights severity to user experience (UX)

## Comparison
<table>
    <tr>
        <th>Name</th> <th>Non-trivial previous experience?</th> <th>Description</th>
        <th>Notes</th>
    </tr>
    <tr>
        <td>HTML forms, no AJAX</td><td>✔️ (25-50% of career)</td>
        <td>Operate with browser built-in form submission, e.g. `&lt;form&gt;` and `&lt;input&gt;`</td>
        <td>
            <a href="https://developer.mozilla.org/en-US/docs/Learn/Forms/Your_first_form">MDN article</a>.
            Works quite well and has good associated UX (progress shown in address bar).
            Extension for improved UX (e.g. loading spinners)
            <br/>
            <br/>
            Major strength is no need to track DB state from browser locally as well as
            easy to build + maintain functionality like links that perform logic and redirects as needed
            <br/>
            <br/>
            Major downside reduced code reuse for <a
                href="https://developer.mozilla.org/en-US/docs/Glossary/SPA"
            >Single-Page Applications (SPA)</a>, but in my experience these are quite rare
            and not the primary purpose of a web app
        </td>
    </tr>
    <tr>
        <td><strong>HTML forms, limited AJAX (winner)</strong></td><td>✔️ (10% of career)</td>
        <td>Use `&lt;form&gt;` and such majority of time, but exit in occasional scenarios like secondary form actions (e.g. notification dismissal)</td>
        <td>
            Same as "HTML forms, no AJAX" but a little more lenient.
            e.g. We don't want UX to suffer for things like dismissing notifications,
            so support those as a one-off
            <br/>
            <br/>
            This was frustrating to deal with in early web days with jQuery due to page specific focus,
            but I think as long as widget-focused approach is used
            (e.g. <a href="https://getbootstrap.com/">Bootstrap</a>,
            <a href="https://www.patterns.dev/posts/islands-architecture">"islands" architecture</a>),
            then it should generally be maintainable and great UX
            <br/>
            <br/>
            Sometimes people might get thrown for things like
            "How do I build an interactive map around with this?"
            <br/>
            In that scenario, I'd make that specific page React-based and build the UI around it,
            but the React would update HTML form content and the submission would happen without obscuring it.
            <br/
            >Or maybe the page is well-contained to self-contain AJAX,
            as long as it's to 1-2 endpoints at most
        </td>
    </tr>
    <tr>
        <td>HTML forms with server-driven HTML updates (e.g. <a href="https://htmx.org/">HTMX</a>)</td>
        <td>✔️ (10% of career)</td>
        <td>Swap content from an HTTP response with a declared target</td>
        <td>
            I rolled our own setup for this in 2013 for https://riders.uber.com/ and deeply regret it.
            <br/>
            It was a good idea on paper (had buy-in from others),
            but in practice it made for awful UX (e.g. no good loading spinners)
            and content swaps felt unexpected.
            <br/>
            Additionally, the actual code seemed fragmented/confusing
            because updates were split across 2 places
            (server saying what to update to, browser saying how to swap).
            <br/>
            Comically, the <a
                href="https://htmx.org/essays/when-to-use-hypermedia/"
            >HTMX author agrees on similar points</a>.
            <br/>I strongly advise against this approach
        </td>
    </tr>
    <tr>
        <td>HTML forms pre-login, AJAX only forms/content after login</td><td></td>
        <td>Leverage Django built-in support for auth pages and cookie sessions to start, but then lean into AJAX only afterwards</td>
        <td>
            Seems like it'd provide a good UX, but I believe it'd destroy developer experience (DX)
            by needing to remember 1 set of rules for some pages, and a different set for another.
            <br/>
            Not to mention double tooling for things like linting (e.g. HTML errors) as well as reduced code reusability.
            <br/>
            Additionally, you still run into the drawbacks of "No HTML forms, AJAX only" like cache management.
            <br/>
            <br/>
            EDIT: I'm later eating my words here (though only in the high interactivity context),
            because this is exactly what I'm recommending =/
            <br/>
            It's prob good to hit the ground running, but may lead to confusion long-term.
            <br/>
            But it's kind of hard to run into issues in the `django-allauth` case since HTML forms are not controlled by us
            <br/>
            whereas the React ones would be
        </td>
    </tr>
    <tr>
        <td>No HTML forms, AJAX only</td><td>✔️ (20% of career)</td>
        <td>Control everything through a SPA, from authentication to page navigation</td>
        <td>
            Works fantastic for things like UI management and dynamically shifting through pages (UX),
            but extremely frustrating when it comes to DB state tracking (DX).
            <br/>
            <br/>
            i.e. For this to work, the SPA needs to effectively have a copy of the API responses,
            and know when 1 save requires breaking the cache of other existing responses.
            <br/>
            <br/>
            This leads to a lot of busy work with little value,
            that could have been avoided with another architecture.
            <br/>
            Additionally, you probably lose a lot of freebies we got from the web framework selection
            (e.g. rebuilding login + sign up + forgot password + sessions).
            <br/>
            Also, if done incorrectly (e.g. not using cookie sessions),
            then it also introduces security issues around HTTP referrers being sent to third party scripts and JWT tokens being unable to be invalidated.
        </td>
    </tr>
</table>
