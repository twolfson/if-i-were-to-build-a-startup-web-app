.. This document is in reStructuredText unlike Markdown the rest of the repo due to needing multi-line support in tables. -->

Development Containment Analysis
================================
**Winner: Language level, nothing else**

**Runner-up: OS level, with or without language level**

Description
-----------
In addition to the `Development Machine </development-machine.md>`_, the application environment/dependencies can be contained and isolated

Comparison
----------
The choices aren't mutually exclusive, they can be combined as needed/wanted -- and some may be redundant with machine choice (e.g. virtual environments on a cloud machine)

+-----------------------------------------------+----------------------------------+---------------------------------------------------------+-------+
|                      Name                     | Non-trivial previous experience? |                       Description                       | Notes |
+===============================================+==================================+=========================================================+=======+
| No containment                                | ✔️ (half of career-ish)          | Nothing isolating dependencies on the machine           |       |
+-----------------------------------------------+----------------------------------+---------------------------------------------------------+-------+
| **Language level (e.g. `Virtual`_) (winner)** | ✔️ (majority)                    | Isolate dependencies through folders                    |       |
+-----------------------------------------------+----------------------------------+---------------------------------------------------------+-------+
| OS level (e.g. `Docker`_, `Vagrant`_)         | ✔️ (half of career-ish)          | Isolate entire OS through either a container or full VM |       |
+-----------------------------------------------+----------------------------------+---------------------------------------------------------+-------+
|                                               |                                  |                                                         |       |

.. _Virtual: https://docs.python.org/3/library/venv.html#venv-def
.. _node_modules: https://docs.npmjs.com/cli/v9/configuring-npm/folders
.. _Docker: https://www.docker.com/
.. _Vagrant: https://www.vagrantup.com/