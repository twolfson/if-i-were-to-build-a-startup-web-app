# Web Framework
Decision: [Django][]

[Django] https://www.djangoproject.com/

## Comparison
|                      Name                      | Non-trivial previous experience? |                  Description                   |                                                                                                                                                                   Notes                                                                                                                                                                   |
|------------------------------------------------|----------------------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AWS Lambda with no framework (Python, Node.js) | ✅ (1 year)                       | Write a function which acts as an endpoint     | It's a great infrastructure for trigger-based runs with dynamic scale, but dependency management has a long way to go. Additionally, it lacks significant ecosystem support so not a good web framework choice at the moment                                                                                                              |
| CodeIgniter (PHP)                              | ✅ (0.5 years)                    | Lightweight framework                          | Only mentioning due to experience. PHP has a lot of baggage with it that's nice to sidestep if possible (e.g. [every page starting with `<?`](https://www.php.net/manual/en/language.basic-syntax.phptags.php))                                                                                                                           |
| Django (Python)                                | ✅ (2 years)                      | Full-fledged framework with batteries included | Significant amount support provided to hit the ground running productively. i.e. ORM, migrations, admin UI, users, thorough ecosystem. Hands down my #1 choice                                                                                                                                                                            |
| Express (Node.js)                              | ✅ (2.5 years)                    | Lightweight framework                          | Only does routing, nothing else. For a startup, table stakes usually involve an ORM (removes relationships as cognitive load + mitigate SQL injection by convention), templates (mitigates XSS by convention), Node.js migration tools (e.g. `sequelize` didn't autocreate from schema) so redoing model work twice. Just not a good idea |
| Flask (Python)                                 | ✅ (3 years)                      |                                                |                                                                                                                                                                                                                                                                                                                                           |
| No framework (PHP)                             | ✅ (0.5 years)                    | Try to get by with no framework at all         | I did this in my high school and college years (2005-2011) (not counted as part of 12 years). The web was still quite young, but it was a terrible experience and I was either arrogant or didn't know much better. I don't recommend it                                                                                                  |
| Rails (Ruby)                                   | ✅ (1 year)                       |                                                |                                                                                                                                                                                                                                                                                                                                           |
| Sails (Node.js)                                |                                  | Full-fledged framework, named after Rails      |                                                                                                                                                                                                                                                                                                                                           |
| Sinatra (Ruby)                                 | ✅ (0.5 years)                    |                                                |                                                                                                                                                                                                                                                                                                                                           |

All years are as full-time equivalents, even from part-time roles pre-2011

TODO: I didn't finish writing out content here, let's finish that

<!-- I'm handwaving Flask to include Pyramid as well, but the switch between Flask <> Pyramid at a company was fuzzy -->

## If I didn't choose Django
If I didn't choose Django, there'd be a lot more additional research and setup work as well:

- Picking an ORM
- Picking a migration tool (if ORM doesn't have it built-in)
    - Additional cost: If migrations aren't autogenerated, then need to write these out every time
- Picking an authentication framework
    - Please never ever roll your own here, it's too easy to get security wrong
- Building an admin UI
    - Additional cost: Building/maintaining infrastructure for admin UI (e.g. permission levels, audit logging)
