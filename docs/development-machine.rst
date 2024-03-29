Development Machine Analysis
============================

**Winner: Local machine**

Runner-up: No others preferred.
A non-production cloud machine (shared or personal) is nice to have but not a good replacement

Description
-----------
Web apps run on a computer either locally or on a machine from a provider, or somewhere in-between.

For development, there's a bunch of choices around "how" to accomplish this --
and the shape of the web app may inform/force certain choices.

Comparison
----------
These choices aren't necessarily exclusive, and it does become personal preference (so a team might support a variety),
but when starting it'll be me and I tend to stick to 1 type most of the time.

+----------------------------+------------------------+--------------------------------+------------------------------------------------------------+
| Name                       | Non-trivial            | Description                    | Notes                                                      |
|                            | previous experience?   |                                |                                                            |
+============================+========================+================================+============================================================+
| **Local machine (winner)** | ✔️ (majority)          | Develop on your local computer | Best experience I've had since there's no lag,             |
|                            |                        |                                | and no jumping through hoops for functionality/features    |
+----------------------------+------------------------+--------------------------------+------------------------------------------------------------+
| Personal cloud machine     | ✔️ (lightly)           | Develop on an instance         | This works alright, but the remote development environment |
|                            |                        | specifically for you           | can be laggy and tooling can feel limited                  |
|                            |                        |                                | (though modern toolkits are getting way better I believe   |
|                            |                        |                                | (`VS Code example <remote-vscode>`_)).                     |
|                            |                        |                                |                                                            |
|                            |                        |                                |                                                            |
|                            |                        |                                | Benefits include easy integration to existing VPC setups,  |
|                            |                        |                                | but when starting those usually aren't needed              |
+----------------------------+------------------------+--------------------------------+------------------------------------------------------------+
| Shared cloud machine       | ✔️ (yes,               | Everyone shares an environment | Every time I've had this, I always have                    |
|                            | but never exclusively) | (e.g. ``beta``, ``staging``)   | local development as well - and I lean into that because   |
|                            |                        | for development                | there's no fear of collisions of work.                     |
|                            |                        |                                |                                                            |
|                            |                        |                                |                                                            |
|                            |                        |                                | Benefits tend to include being a downstream                |
|                            |                        |                                | scrubbed replica of production more easily                 |
+----------------------------+------------------------+--------------------------------+------------------------------------------------------------+
| Production only            |                        | Everyone shares the            | I've thankfully never had to experience this.              |
|                            |                        | same production environment    | Very risky due to edits affecting people using application |
+----------------------------+------------------------+--------------------------------+------------------------------------------------------------+

.. _`remote-vscode`: https://code.visualstudio.com/docs/remote/remote-overview
