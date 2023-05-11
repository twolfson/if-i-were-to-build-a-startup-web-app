# Web Framework
## Decision
Django, https://www.djangoproject.com/

## Comparison
|                      Name                      | Non-trivial previous experience? |                  Description                   |                                                                                                                         Notes                                                                                                                          |
|------------------------------------------------|----------------------------------|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AWS Lambda with no framework (Python, Node.js) | ✔️ (1 year)                      | Write a function which acts as an endpoint     | It's a great infrastructure for trigger-based runs (e.g. S3 upload) with dynamic scale, but dependency management has a long way to go.<br/><br/>Additionally, it lacks significant ecosystem support so not a good web framework choice at the moment |
| CodeIgniter (PHP)                              | ✔️ (0.5 years)                   | Lightweight framework                          | Only mentioning due to experience. PHP has a lot of baggage with it that's nice to sidestep if possible (e.g. [every page starting with `<?`](https://www.php.net/manual/en/language.basic-syntax.phptags.php))                                        |
| **Django (Python) (decision)**                 | ✔️ (2 years)                     | Full-fledged framework with batteries included | Significant amount support provided to hit the ground running productively.<br/>i.e. ORM, migrations, admin UI, users, thorough ecosystem                                                                                                              |
| Express (Node.js)                              | ✔️ (2.5 years)                   | Lightweight framework                          | Only does routing, nothing else (e.g. no ORM, no templates, no migration tools) (elaboration at bottom).<br/>Would need to pick and integrate additional pieces. Just not a good idea                                                                  |
| Flask (Python)                                 | ✔️ (3 years)                     | Lightweight framework                          | Routing -- TODO: Continue writing...                                                                                                                                                                                                                                                       |
| No framework (PHP)                             | ✔️ (0.5 years)                   | Try to get by with no framework at all         | I did this in my high school and college years (2005-2011) (not counted as part of 12 years). The web was still quite young, but it was a terrible experience and I was either arrogant or didn't know much better. I don't recommend it               |
| Rails (Ruby)                                   | ✔️ (1 year)                      |                                                |                                                                                                                                                                                                                                                        |
| Sails (Node.js)                                |                                  | Full-fledged framework, named after Rails      |                                                                                                                                                                                                                                                        |
| Sinatra (Ruby)                                 | ✔️ (0.5 years)                   |                                                |                                                                                                                                                                                                                                                        |

All years are as full-time equivalents, even from part-time roles pre-2011

TODO: I didn't finish writing out content here, let's finish that

<!-- I'm handwaving Flask to include Pyramid as well, but the switch between Flask <> Pyramid at a company was fuzzy -->

<!--
    DEV: There's no built-in way to do linebreaks in Markdown tables,
    so using <br/> (though could do full <table> for consistency),
    https://stackoverflow.com/a/41313478 + https://www.markdownguide.org/hacks/#line-breaks-within-table-cells
-->

## If I didn't choose Django
If I didn't choose Django, there'd be a lot more additional research and setup work as well:

- Picking a router (if not built-in)
    - This is a core feature in most frameworks, but if going "No framework", then would need to pick or build
- Picking an ORM (e.g. SQLAlchemy, sequelize)
    - Why we want one:
        - Removes cognitive load around what a join was for a given relationship, on every query
        - Mitigates SQL injection by convention
- Picking a migration tool (if ORM doesn't have it built-in) (e.g. alembic, raw SQL files)
    - Additional cost: If migrations aren't autogenerated, then need to write these out every time
- Picking a template (e.g. Jinja, Mustache, EJS)
    - Why we want this:
        - Allows easier expression and maintenance of HTML
        - Mitigates XSS attacks by convention
- Picking an authentication framework (e.g. Passport, Flask-Login)
    - Please never ever roll your own here, it's too easy to get security wrong
- Building an admin UI (in contrast to Django Admin and Rails Admin)
    - Additional cost: Building/maintaining infrastructure for admin UI (e.g. permission levels, audit logging)
- Building testing infrastructure
    - Either need to stand up server on its own, or X

For items listed as "picking", you could also build one obviously, but I wouldn't recommend it. They're solved problems.

Again, the goal of a startup is to deliver value to others. Time spent rebuilding solved problems is time that could be creating value instead.
