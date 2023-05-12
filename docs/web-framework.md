# Web Framework
## Decision
**Winner: Django, https://www.djangoproject.com/**

**Runner-up: Ruby on Rails, https://rubyonrails.org/**

Django has batteries included for everything you'd ever want, plus a wonderful ecosystem for things beyond that (e.g. [history](https://django-simple-history.readthedocs.io/), [enhancements](https://django-extensions.readthedocs.io/)). And to top it off, it's built on Python, which itself has a thriving ecosystem.

Ruby on Rails is also quite strong, but I'm less of a fan due to Ruby feeling like it's not as strong of an ecosystem and being a language with unavoidable footguns (e.g. implicit returns, implicit parentheses).

## Comparison
|                      Name                      | Non-trivial previous experience? |                  Description                   |                                                                                                                         Notes                                                                                                                          |
|------------------------------------------------|----------------------------------|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AWS Lambda][] with no framework (Python, Node.js) | ✔️ (1 year)                      | Write a function which acts as an endpoint     | It's a great infrastructure for trigger-based runs (e.g. S3 upload) with dynamic scale, but dependency management has a long way to go.<br/><br/>Additionally, it lacks significant ecosystem support so not a good web framework choice at the moment |
| [CodeIgniter][] (PHP)                              | ✔️ (0.5 years)                   | Lightweight framework                          | Only mentioning due to experience. PHP has a lot of baggage with it that's nice to sidestep if possible (e.g. [every page starting with `<?`](https://www.php.net/manual/en/language.basic-syntax.phptags.php))                                        |
| **[Django][] (Python) (winner)**                 | ✔️ (2 years)                     | Full-fledged framework with batteries included | Significant amount support provided to hit the ground running productively (e.g. ORM, migrations, admin UI, users, thorough ecosystem)                                                                                                              |
| [Express][] (Node.js)                              | ✔️ (2.5 years)                   | Lightweight framework                          | Only does routing and template integration, and basic request handling. There is a [generator utility](https://expressjs.com/en/starter/generator.html) but it's only for initial setup.<br/><br/>There are no built-ins for ORM, no migration tools, no admin UI, and multipart forms [requires adding a parser](https://expressjs.com/en/5x/api.html#req.properties). Just not a good idea (elaboration at bottom)                                                                 |
| [Flask][] (Python)                                 | ✔️ (3 years)                     | Lightweight framework                          | Similar to [Express][] but a little more robust. Provides routing, templates, sessions, and multipart form support.<br/><br/>Lacks ORM, though [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) is popular, but that lacks migrations ([alembic](https://alembic.sqlalchemy.org/) is popular), and you keep running into little nags like that                                                                                                                 |
| No framework (PHP)                             | ✔️ (0.5 years)                   | Try to get by with no framework at all         | I did this 2008-2011 when I was in college. The web was still quite young, but it was a terrible experience. I don't recommend it               |
| [Ruby on Rails][] (Ruby)                                   | ✔️ (1 year)                      | Full-fledged framework with batteries included                                               | Provies wonderful built-ins like ORM and migrations, with some admin options through its ecosystem (e.g. [Rails Admin](https://rails.devcamp.com/trails/ruby-gem-walkthroughs/campsites/admin-dashboard-gems/guides/rails-admin-gem-tutorial)).<br/>It was great to use, except for the parentheses confusion that Ruby encourages and the testing felt clunky to interface with at times (both minor)                                                                                                                                                                                                                                                      |
| [Sails][] (Node.js)                                |                                  | Full-fledged framework, named after Rails      | Generally provides a lot of features (e.g. ORM, templates, sessions) but [falls short on migrations](https://sailsjs.com/documentation/concepts/models-and-orm/model-settings#database-migrations) (manual preferred for live data) and nothing for admin UI.<br/>They've made a lot of progress over the years, but I'd be hesitant to [use an innovation token here](https://mcfunley.com/choose-boring-technology)                                                                                                                                                                                                                                                       |
| [Sinatra][] (Ruby)                                 | ✔️ (0.5 years)                   | Lightweight framework                                               | Provides routing, templates, and sessions support but on your own for ORM, migrations, and admin UI. It was a comparable experience to Flask iirc                                                                                                                                                                                                                                                       |

[AWS Lambda]:https://aws.amazon.com/lambda/
[CodeIgniter]: https://codeigniter.com/
[Django]: https://www.djangoproject.com/
[Express]: https://expressjs.com/
[Flask]: https://flask.palletsprojects.com/
[Ruby on Rails]: https://rubyonrails.org/
[Sails]: https://sailsjs.com/
[Sinatra]: https://sinatrarb.com/

All years stated above are as full-time equivalents, even from part-time roles pre-2011

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
