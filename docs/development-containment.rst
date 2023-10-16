Development Containment Analysis
================================

.. Raw HTML support due to rST not supporting inline formatting + links, https://docutils.sourceforge.io/FAQ.html#is-nested-inline-markup-possible
   There's also | syntax, but that is tricky for editing with tables, so using :raw-html:, https://stackoverflow.com/a/51199504/1960509

.. role:: raw-html(raw)

    :format: html

Decision
--------

**Winner: Language level, nothing else**

**Runner-up: OS level, with or without language level**

Description
-----------
In addition to the `Development Machine <./development-machine.md>`_, the application environment/dependencies can be contained and isolated

Comparison
----------
The choices aren't mutually exclusive, they can be combined as needed/wanted -- and some may be redundant with machine choice (e.g. virtual environments on a cloud machine)

+--------------------------+-------------------------+--------------------------------+-----------------------------------------------------------------------------------------------------------+
| Name                     | Non-trivial             | Description                    | Notes                                                                                                     |
|                          | previous experience?    |                                |                                                                                                           |
+==========================+=========================+================================+===========================================================================================================+
|                          |                         |                                |                                                                                                           |
| No containment           | ✔️ (half of career-ish) | Nothing isolating dependencies | This only happens with languages which use                                                                |
|                          |                         | on the machine                 | system-wide dependencies by default (e.g. Python and ``pip``).                                            |
|                          |                         |                                |                                                                                                           |
|                          |                         |                                |                                                                                                           |
|                          |                         |                                | It's risky if it's your local computer,                                                                   |
|                          |                         |                                | because dependencies for unrelated things (e.g. your music player)                                        |
|                          |                         |                                | may conflict with your application's ones                                                                 |
|                          |                         |                                |                                                                                                           |
+--------------------------+-------------------------+--------------------------------+-----------------------------------------------------------------------------------------------------------+
|                          |                         |                                |                                                                                                           |
| :raw-html:`<strong>`     | ✔️ (majority)           | Isolate dependencies           | Provides sane isolation without concerns of something unrelated unexpectedly leading to conflict,         |
| Language level (e.g.     |                         | through folders                | :raw-html:`<br/>`                                                                                         |
| `Virtual Environments`_, |                         |                                | as well as ability to easily inspect and adjust dependencies if needed (rare)                             |
| `node_modules`_)         |                         |                                |                                                                                                           |
| (winner)                 |                         |                                |                                                                                                           |
| :raw-html:`</strong>`    |                         |                                | For non-built-in (e.g. Virtual Environments), there's an extra lift of always invoking the shell wrapper  |
|                          |                         |                                | (e.g. ``bin/activate``) (unless shell auto-invokes) but OS level has similar drawbacks                    |
|                          |                         |                                |                                                                                                           |
+--------------------------+-------------------------+--------------------------------+-----------------------------------------------------------------------------------------------------------+
|                          |                         |                                |                                                                                                           |
| OS level (e.g.           | ✔️ (half of career-ish) | Isolate entire OS through      | As close as possible to production environment,                                                           |
| `Docker`_,               |                         | either a container or full VM  | if not 1:1 due to using same solution in production.                                                      |
| `Vagrant`_)              |                         |                                |                                                                                                           |
|                          |                         |                                |                                                                                                           |
|                          |                         |                                | In practice, it's rare that an OS-specific issue is seen again in production                              |
|                          |                         |                                | (unless you develop on Windows and interface with paths)                                                  |
|                          |                         |                                |                                                                                                           |
|                          |                         |                                |                                                                                                           |
|                          |                         |                                | Drawbacks include needing to enter the container shell every time and deal with folder mounting/isolation |
|                          |                         |                                |                                                                                                           |
+--------------------------+-------------------------+--------------------------------+-----------------------------------------------------------------------------------------------------------+

.. _`Virtual Environments`: https://docs.python.org/3/library/venv.html#venv-def
.. _`node_modules`: https://docs.npmjs.com/cli/v9/configuring-npm/folders

.. _`Docker`: https://www.docker.com/
.. _`Vagrant`: https://www.vagrantup.com/
