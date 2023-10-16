Web Framework Analysis
======================

.. Raw HTML support due to rST not supporting inline formatting + links, https://docutils.sourceforge.io/FAQ.html#is-nested-inline-markup-possible
   There's also | syntax, but that is tricky for editing with tables, so using :raw-html:, https://stackoverflow.com/a/51199504/1960509

.. role:: raw-html(raw)

    :format: html

Decision
--------
:raw-html:`<strong>` Winner: Django, https://www.djangoproject.com/ :raw-html:`</strong>`

:raw-html:`<strong>` Runner-up: Ruby on Rails, https://rubyonrails.org/ :raw-html:`</strong>`

Django has batteries included for everything you'd ever want, plus a wonderful ecosystem for things beyond that (e.g. `history <https://django-simple-history.readthedocs.io/>`_, `enhancements <https://django-extensions.readthedocs.io/>`_). And to top it off, it's built on Python, which itself has a thriving ecosystem.

Ruby on Rails is also quite strong, but I'm less of a fan due to Ruby feeling like it's not as strong of an ecosystem and being a language with unavoidable footguns (e.g. implicit returns, implicit parentheses).

Description
-----------
A web framework is a foundational layer and system for building a web application within. It provides many features and functionality to get a product built as rapidly as possible. Full enumeration of such features is at the bottom of this file.

Comparison
----------
+--------------------------------+----------------------+--------------------------+----------------------------------------------------------------------+
| Name                           | Non-trivial          | Description              | Notes                                                                |
|                                | previous experience? |                          |                                                                      |
+================================+======================+==========================+======================================================================+
| `AWS Lambda`_ with             | ✔️ (1 year)          | Write a function which   | It's a great infrastructure for trigger-based runs                   |
| no framework (Python, Node.js) |                      | acts as an endpoint      | (e.g. S3 upload) with dynamic scale,                                 |
|                                |                      |                          | but dependency management has a long way to go.                      |
|                                |                      |                          |                                                                      |
|                                |                      |                          |                                                                      |
|                                |                      |                          | Additionally, it lacks significant ecosystem support                 |
|                                |                      |                          | so not a good web framework choice at the moment                     |
+--------------------------------+----------------------+--------------------------+----------------------------------------------------------------------+
| `CodeIgniter`_ (PHP)           | ✔️ (0.5 years)       | Lightweight framework    | Only mentioning due to experience.                                   |
|                                |                      |                          | PHP has a lot of baggage with it                                     |
|                                |                      |                          | that's nice to sidestep if possible                                  |
|                                |                      |                          | (e.g. `every page starting with \<? PHP tags <PHP tags_>`_)          |
+--------------------------------+----------------------+--------------------------+----------------------------------------------------------------------+
| :raw-html:`<strong>`           | ✔️ (2 years)         | Full-fledged framework   | Significant amount support provided to                               |
| `Django`_ (Python) (winner)    |                      | with batteries included  | hit the ground running productively                                  |
| :raw-html:`</strong>`          |                      |                          | (e.g. ORM, migrations, admin UI, users, thorough ecosystem)          |
+--------------------------------+----------------------+--------------------------+----------------------------------------------------------------------+
| `Express`_ (Node.js)           | ✔️ (2.5 years)       | Lightweight framework    | Only does routing and template integration,                          |
|                                |                      |                          | and basic request handling.                                          |
|                                |                      |                          | There is a `generator utility <Express generator_>`_                 |
|                                |                      |                          | but it's only for initial setup.                                     |
|                                |                      |                          |                                                                      |
|                                |                      |                          |                                                                      |
|                                |                      |                          | There are no built-ins for ORM, no migration tools,                  |
|                                |                      |                          | no admin UI, and multipart forms                                     |
|                                |                      |                          | `requires adding a parser <Express parser_>`_.                       |
|                                |                      |                          | Just not a good idea (elaboration at bottom)                         |
+--------------------------------+----------------------+--------------------------+----------------------------------------------------------------------+
| `Flask`_ (Python)              | ✔️ (3 years)         | Lightweight framework    | Similar to Express but a little more robust.                         |
|                                |                      |                          | Provides routing, templates, sessions, and multipart form support.   |
|                                |                      |                          |                                                                      |
|                                |                      |                          |                                                                      |
|                                |                      |                          | Lacks ORM, though `Flask-SQLAlchemy`_ is popular,                    |
|                                |                      |                          | but that lacks migrations (`alembic`_ is popular),                   |
|                                |                      |                          | and you keep running into little nags like that                      |
+--------------------------------+----------------------+--------------------------+----------------------------------------------------------------------+
| No framework (PHP)             | ✔️ (0.5 years)       | Try to get by            | I did this 2008-2011 when I was in college.                          |
|                                |                      | with no framework at all | The web was still quite young, but it was a terrible experience.     |
|                                |                      |                          | I don't recommend it                                                 |
+--------------------------------+----------------------+--------------------------+----------------------------------------------------------------------+
| `Ruby on Rails`_ (Ruby)        | ✔️ (1 year)          | Full-fledged framework   | Provies wonderful built-ins like ORM and migrations,                 |
|                                |                      | with batteries included  | with some admin options through its ecosystem (e.g. `Rails Admin`_). |
|                                |                      |                          | :raw-html:`<br/>`                                                    |
|                                |                      |                          | It was great to use, except for                                      |
|                                |                      |                          | the parentheses confusion that Ruby encourages                       |
|                                |                      |                          | and the testing felt clunky to interface with at times               |
|                                |                      |                          | (both minor)                                                         |
+--------------------------------+----------------------+--------------------------+----------------------------------------------------------------------+
| `Sails`_ (Node.js)             |                      | Full-fledged framework,  | Generally provides a lot of features (e.g. ORM, templates, sessions) |
|                                |                      | named after Rails        | but `falls short on migrations <Sails migrations_>`_)                |
|                                |                      |                          | (manual preferred for live data) and nothing for admin UI.           |
|                                |                      |                          | :raw-html:`<br/>`                                                    |
|                                |                      |                          | They've made a lot of progress over the years,                       |
|                                |                      |                          | but I'd be hesitant to                                               |
|                                |                      |                          | `use an innovation token here <Innovation token_>`_                  |
+--------------------------------+----------------------+--------------------------+----------------------------------------------------------------------+
| `Sinatra`_ (Ruby)              | ✔️ (0.5 years)       | Lightweight framework    | Provides routing, templates, and sessions support                    |
|                                |                      |                          | but on your own for ORM, migrations, and admin UI.                   |
|                                |                      |                          | It was a comparable experience to Flask iirc                         |
+--------------------------------+----------------------+--------------------------+----------------------------------------------------------------------+
| Other frameworks               |                      |                          | There are many frameworks out there.                                 |
|                                |                      |                          | This is simply a list from experience, top of mind,                  |
|                                |                      |                          | and light searching                                                  |
+--------------------------------+----------------------+--------------------------+----------------------------------------------------------------------+

.. _`AWS Lambda`: https://aws.amazon.com/lambda/
.. _`CodeIgniter`: https://codeigniter.com/
.. _`Django`: https://www.djangoproject.com/
.. _`Express`: https://expressjs.com/
.. _`Flask`: https://flask.palletsprojects.com/
.. _`Ruby on Rails`: https://rubyonrails.org/
.. _`Sails`: https://sailsjs.com/
.. _`Sinatra`: https://sinatrarb.com/

.. _`PHP tags`: https://www.php.net/manual/en/language.basic-syntax.phptags.php
.. _`Express generator`: https://expressjs.com/en/starter/generator.html
.. _`Express parser`: https://expressjs.com/en/5x/api.html#req.properties
.. _`Flask-SQLAlchemy`: https://flask-sqlalchemy.palletsprojects.com/
.. _`alembic`: https://alembic.sqlalchemy.org/
.. _`Rails Admin`: https://rails.devcamp.com/trails/ruby-gem-walkthroughs/campsites/admin-dashboard-gems/guides/rails-admin-gem-tutorial
.. _`Sails migrations`: https://sailsjs.com/documentation/concepts/models-and-orm/model-settings#database-migrations
.. _`Innovation token`: https://mcfunley.com/choose-boring-technology

All years stated above are as full-time equivalents, even from part-time roles pre-2011

.. I'm handwaving Flask to include Pyramid as well, but the switch between Flask <> Pyramid at a company was fuzzy

Everything We're Considering
----------------------------
By going with Django, I sidestep a lot of research, integration, and maintenance work for each of the features below.

As a reminder, the goal of a startup is to deliver value to others. The following are all solved problems.
:raw-html:`<br/>`
Time spent rebuilding solved problems is time that could be creating value instead.

Fundamentals
------------
- Routing

  - What: Indicate a given function to respond to a given HTTP URL and method

  - Why: Web apps respond to different requests, so isolating request to different functions enables code isolation


- ORM (e.g. SQLAlchemy, sequelize)

  - What: Allows interacting with a database through a language-native interface

  - Why:

    - Removes cognitive load around what a join was for a given relationship, on every query

    - Mitigates SQL injection by convention

    - Encourages relational lookups from a given request to avoid violating access control


- Template engine (e.g. Jinja, Mustache, EJS)

  - What: Interact with template files outside of controllers to generate response content

  - Why:

    - Allows easier expression and maintenance of HTML

    - Mitigates XSS attacks by convention


- Migration tool (e.g. alembic, raw SQL files)

  - What: System to apply isolated schema changes to database in a given order

  - Why:

    - Database schemas change over time, and providing a system to introduce/track those is necessary

    - Autogeneration tied to ORM strongly preferred. If we don't, then we have an additional cost to write both model updates and migrations every change. And schema changes happen often (businesses develop and grow)

      - Django ORM and ActiveRecord have been the only tools I've seen with autogeneration


- Sessions

  - What: Identify an HTTP request from a client (e.g. browser) as the same client on subsequent requests

  - Why:

    - Without sessions, you'd effectively be prompting for authentication criteria on every request (i.e. username + password)

  - How:

    - These can either be implemented through cookies or databases (with browsers storing a cookie identifier)

    - Databases are slightly preferrable since they allow for remote invalidation

    - If selecting a library, try to find one using HMAC - to avoid attackers from tampering with the browser cookie (either identifier or as store)


- Multipart form upload

  - What: :raw-html:`<code><a href="https://everything.curl.dev/http/multipart">multipart/form-data</a></code>` is the only HTTP ``Content-Type`` which supports uploading files along other form data. Supporting it is an eventuality of any web app

  - Why: Web apps will eventually need file upload for some reason (e.g. profile photo, attachments). I prefer to have this from the start, rather than needing to integrate and test said integration


- Users and authentication (AuthN) (e.g. Passport.js, Flask-Login)

  - What: Endpoints for users to sign up, login, perform "reset password", and change password

  - Why: A web app typically operate around interacting with person. User models will faciliate tracking this data, and authentication will associate a session with the user

  - How:

    - For built-in support, this requires an ORM and sessions in the framework. I've only seen this built-in on Django

      - Though even Django is annoying without using ``django-allauth``

    - If you need to set this up, always use an off the shelf library. It's near impossible to get right the first time without introducing security issues


- Admin UI (e.g. Django Admin, Rails Admin)

  - What: Internal tool to allow non-programmers (and programmers) to inspect and take actions (more than direct edits) on models

  - Why:

    - Engineers should never be the bottleneck for inspecting data or taking actions. It's inefficient time and cost-wise for a business

    - Instead, self-serve approaches are better because they remove the need for communication entirely

    - Additional reading: https://twolfson.com/2022-07-30-startup-time-investing-operational-processes

  - How: For systems without built-in admin tools, there are a few options:

    - Either build your own (ideally leveraging the underlying users + sessions infrastructure, but granting admin permissions)

    - or use products like `Retool <https://retool.com/>`_

      - The downside to products is you're either directly exposing your DB (and thus replicate business logic, leading to code drift/errors) OR you're building an API for the products to interface with (additional work + testing)

    - or expose underlying DB through a modifiable interface (e.g. Airtable, Google Sheets) (same issue as direct exposure for Retool)


- Testing infrastructure

  - What: Providing built-in utilities for running performant tests out of the gate (e.g. `Django provides fixtures support <https://docs.djangoproject.com/en/4.2/topics/testing/tools/#django.test.TransactionTestCase.fixtures>`_)

  - Why:

    - Testing can be tedious to set up right at first, and then it can run into performance issues (e.g. setting up fixtures for every test function)

    - Instead, it's easier to get this from the start from the framework

  - How:

    - For some frameworks, this is so bad in that you might run a server and generate requests against it (rather than talking to the controller directly)

    - I've found this is viable yet costs a lot of time, which could have been avoided

    - Try to interface directly with controllers and get good performance by leveraging database rollbacks across groups of tests


Great to Have
-------------
- Authorization (AuthZ)

  - What: Permission to take certain actions at a given endpoint or on a given model

  - Why: Basic access control should be handled by ORM relational lookups, but sometimes multiple users in an account might have different permission levels (e.g. view only). This helps manage that


Nice to Have
------------
- Scripting support

  - What: Infrastructure to run scripts, rather than writing or including your own

  - Why:

    - Django has some basic utilities for commands, like running them in tests

    - Though honestly, extending them has proven a lot more valuable (e.g. distinguishing ``--live-run`` from ``--dry-run``, building ``--persist-temp``)

- Interactive shell with server awareness

  - What: REPL for running one-off queries and updates where scripting would be excessive

  - Why:

    - In rare occasions, manual updates are needed for data (e.g. backfill script went awry, special flag needs setting), it's good

    - You get this for free with a typical REPL, but server awareness (e.g. :raw-html:`<a href="https://django-extensions.readthedocs.io/en/latest/shell_plus.html"><code>shell_plus</code> from <code>django-extensions</code></a>`)

- Ability to output SQL for catching ``n+1`` errors in any scenario

  - What: Outputting SQL in various scenarios (e.g. running server, running commands) can help catch and resolve performance errors like ``n+1`` queries

  - Why: ``n+1`` queries can make a 1 second query for 30,000 rows instead take 30,000 seconds

  - How:

    - ``runserver_plus`` and ``shell_plus`` from ``django-extensions`` both provide a ``--print-sql`` flag

    - For commands, we had to build our own support for this, but it's a direct reuse of the work from ``django-extensions``


Apathetic Mentions
------------------
- Generator utilities

  - What: Built-in commands to help generate new models and controllers

  - Why:

    - It's intended for time saving

    - but usually there's time spent reading + modifying, and I believe that's equivalent to copy/pasting from existing code (hence apathy)

    - Ruby on Rails provides these utilities, https://guides.rubyonrails.org/command_line.html#bin-rails-generate
