Database Analysis
=================

.. Raw HTML support due to rST not supporting inline formatting + links, https://docutils.sourceforge.io/FAQ.html#is-nested-inline-markup-possible
   There's also | syntax, but that is tricky for editing with tables, so using :raw-html:, https://stackoverflow.com/a/51199504/1960509

.. role:: raw-html(raw)

    :format: html

Decision
--------

:raw-html:`<strong>` Winner: PostgreSQL, https://www.postgresql.org/ :raw-html:`</strong>`

:raw-html:`<strong>` Runner-up: MySQL/MariaDB, https://mariadb.org/ :raw-html:`</strong>`

Explanations in comparison table

Description
-----------
A database in the context of a web app is service/system that stores data for users interact with.

For the sake of this discussion, I'll be interchanging **relational** with **SQL** and **non-relational** with **NoSQL** freely. I don't believe there's distinctions respectively, but I could be wrong here.

`Non-relational/NoSQL <https://en.wikipedia.org/wiki/NoSQL>`_ encompasses many database types with different data structures:
- Key-value, like Redis and Memcached
- Document, like MongoDB
- and pretty much anything else that's not tabular with relationships between them

`Relational/SQL <https://en.wikipedia.org/wiki/Relational_database>`_ is strictly tables and relationships between them (e.g. MySQL, PostgreSQL).

Comparison
----------

+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| Name                      | Non-trivial          | Description                 | Notes                                                                   |
|                           | previous experience? |                             |                                                                         |
+===========================+======================+=============================+=========================================================================+
| DIY text files            | ✔️ (0.5 years)       | Make your own DB solution   | I did this 2008-2011 when I was in college.                             |
|                           |                      | through ``.txt`` files      | I was trying to save costs from running a server,                       |
|                           |                      |                             | but it was a terrible experience due to custom formats                  |
|                           |                      |                             | and concurrency issues.                                                 |
|                           |                      |                             | Thankfully the sites were barely used                                   |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| `DynamoDB`_               |                      | Key-value store (NoSQL)     | I've only heard the name but it seems to                                |
|                           |                      |                             | mostly be a key-value store like Memcached and Redis. See Redis' notes  |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| `Elasticsearch`_          | ✔️ (1.5 years)       | JSON document search        | Elasticsearch is built as a search engine, not as a DB store.           |
|                           |                      | engine (NoSQL)              | It's included because it's NoSQL,                                       |
|                           |                      |                             | but it's not a fit as the primary store of a web app                    |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| `Firebase`_               |                      | Document store (NoSQL)      | Technically 2 products, `Firestore`_ and Realtime Database              |
|                           |                      |                             | but I believe the underlying systems are both document stores.          |
|                           |                      |                             |                                                                         |
|                           |                      |                             |                                                                         |
|                           |                      |                             | As a result, they're prone to the same issues as MongoDB as well as     |
|                           |                      |                             | not having a dedicated server for business logic,                       |
|                           |                      |                             | meaning additional work with their functions                            |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| `Google Sheets/Airtable`_ | ✔️ (0.25 years)      | "Relational" DB             | Technically anything stored in a relational database                    |
| as DB                     |                      |                             | can also be stored in a spreadsheet.                                    |
|                           |                      |                             | This has the benefit of being transparent/modifiable immediately.       |
|                           |                      |                             | :raw-html:`<br/>`                                                       |
|                           |                      |                             | However, since we chose Django, we get Django Admin                     |
|                           |                      |                             | so we have easy exposure as-is                                          |
|                           |                      |                             |                                                                         |
|                           |                      |                             |                                                                         |
|                           |                      |                             | These are still solid for MVP explorations (e.g. form submission)       |
|                           |                      |                             | but not long-term (e.g. no constraints, no foreign keys,                |
|                           |                      |                             | bad at concurrency)                                                     |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| `Memcached`_              | ✔️ (0.1 years)       | Key-value store (NoSQL)     | Comparable to Redis, see its notes                                      |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| `MongoDB`_                | ✔️ (0.1 years)       | Document store (NoSQL)      | Lots of traction but also lots of bad growth history.                   |
|                           |                      |                             | I don't have much experience with it.                                   |
|                           |                      |                             | :raw-html:`<br/>`                                                       |
|                           |                      |                             | My understanding of `denormalization`_                                  |
|                           |                      |                             | which requires duplicating data across documents is concerning,         |
|                           |                      |                             | especially from a scaling perspective.                                  |
|                           |                      |                             | And beginners won't learn about it                                      |
|                           |                      |                             | until they're well bought into the system                               |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| `MySQL/MariaDB`_          | ✔️ (4.75 years)      | Relational DB               | Fantastic tool with limited footguns                                    |
|                           |                      |                             | (e.g. always sort by primary key by default)                            |
|                           |                      |                             | but a lot of shortcomings for developer efficiency                      |
|                           |                      |                             | :raw-html:`<br/>`                                                       |
|                           |                      |                             | (e.g. schema changes cannot be done in transactions                     |
|                           |                      |                             | (`MariaDB docs <MariaDB transactions_>`_)                               |
|                           |                      |                             | - so partial migrations can exit in broken state,                       |
|                           |                      |                             | bulk creation doesn't return ids for MySQL and prior to MariaDB 10.5    |
|                           |                      |                             | (`Django docs <Django bulk creation ids_>`_),                           |
|                           |                      |                             | doesn't support unique constraints with conditions                      |
|                           |                      |                             | (`Django docs <Django UniqueConstraint support_>`_))                    |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| :raw-html:`<strong>`      | ✔️ (4.25 years)      | Relational DB               | Amazing database with wonderful ecosystem.                              |
| `PostgreSQL`_ (winner)    |                      |                             | It does have some footguns (e.g. no default sort)                       |
| :raw-html:`</strong>`     |                      |                             | but its pros far outweigh those (e.g. handles cons of MySQL,            |
|                           |                      |                             | friendlier CLI than ``mysql``)                                          |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| `Redis`_                  | ✔️ (2 years)         | Key-value store (NoSQL)     | Wonderful tool to cache values                                          |
|                           |                      |                             | (e.g. HTTP responses, DB lookups, sessions)                             |
|                           |                      |                             | but unreasonable to use as a persistent storage system.                 |
|                           |                      |                             | :raw-html:`<br/>`                                                       |
|                           |                      |                             | It was not designed for that, and values are limited                    |
|                           |                      |                             | in their capabilities                                                   |
|                           |                      |                             | (e.g. would be serializing JSON,                                        |
|                           |                      |                             | which then can't have nested queries)                                   |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| `RocksDB`_                |                      | Key-value store             | Same drawbacks as Redis (key-value store)                               |
|                           |                      | through local files (NoSQL) | but with no provider drawbacks of SQLite (local file)                   |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| `SQLite`_                 | ✔️ (0.1 years)       | Relational DB,              | Quite a powerful tool and sidesteps running a DB server.                |
|                           |                      | stored as local file        | I've used it through one-off scenarios like                             |
|                           |                      |                             | `GeoPackages <GeoPackage>`_                                             |
|                           |                      |                             | but I'd be concerned about using it as the database long-term.          |
|                           |                      |                             |                                                                         |
|                           |                      |                             |                                                                         |
|                           |                      |                             | Due to no provider, there's no automated backups                        |
|                           |                      |                             | (so building your own) as well as potential                             |
|                           |                      |                             | distributed systems issues if introduce multiple servers                |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| User files                |                      | Let user open               | I've played with this for personal projects,                            |
|                           |                      | and save files locally      | but it's a partial solution (and frustrating one if browser closes)     |
|                           |                      |                             | when most users expect the company to persist their data                |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+
| Other databases           |                      |                             | There are many databases out there.                                     |
|                           |                      |                             | This is simply a list from experience, top of mind, and light searching |
+---------------------------+----------------------+-----------------------------+-------------------------------------------------------------------------+

.. _`DynamoDB`: https://aws.amazon.com/dynamodb/t
.. _`Elasticsearch`: https://en.wikipedia.org/wiki/Elasticsearch
.. _`Firebase`: https://firebase.google.com/products/firestore

.. _`Firestore`: https://firebase.google.com/products/firestore
.. _`Realtime Database`: https://firebase.google.com/products/realtime-database

.. _`Google Sheets/Airtable`: https://www.google.com/sheets/about/
.. _`Memcached`: https://memcached.org/
.. _`MongoDB`: https://www.mongodb.com/

.. _`denormalization`: https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design

.. _`MySQL/MariaDB`: https://mariadb.org/
.. _`MariaDB transactions`: https://mariadb.com/kb/en/start-transaction/#ddl-statements
.. _`Django bulk creation ids`: https://github.com/django/django/blob/4.2.1/django/db/backends/mysql/features.py#L195-L201
.. _`Django UniqueConstraint support`: https://github.com/django/django/blob/4.2.1/django/db/models/base.py#L2312-L2331

.. _`PostgreSQL`: https://www.postgresql.org/
.. _`Redis`: https://redis.io/
.. _`RocksDB`: https://rocksdb.org/
.. _`SQLite`: https://sqlite.org/index.html

.. _`GeoPackage`: https://en.wikipedia.org/wiki/GeoPackage
