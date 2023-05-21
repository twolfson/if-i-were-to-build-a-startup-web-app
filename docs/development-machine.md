# Development Machine Analysis
**Winner: Local machine**

Runner-up: No others preferred. A non-production cloud machine (shared or personal) is nice to have but not a good replacement

## Description
Web apps run on a computer either locally or on a machine from a provider, or somewhere in-between.

For development, there's a bunch of choices around "how" to accomplish this -- and the shape of the web app may inform/force certain choices.

## Comparison
These choices aren't necessarily exclusive, and it does become personal preference (so a team might support a variety), but when starting it'll be me and I tend to stick to 1 type most of the time.

|            Name            | Non-trivial previous experience? |                               Description                               |                                                                                                                                                        Notes                                                                                                                                                        |
|----------------------------|----------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Local machine (winner)** | ✔️ (majority)                    | Develop on your local computer                                          | Best experience I've had since there's no lag, and no jumping through hoops for functionality/features                                                                                                                                                                                                              |
| Personal cloud machine     | ✔️ (lightly)                     | Develop on an instance specifically for you                             | This works alright, but the remote development environment can be laggy and tooling can feel limited (though modern toolkits are getting way better I believe ([VS Code example][remote-vscode])).<br/><br/>Benefits include easy integration to existing VPC setups, but when starting those usually aren't needed |
| Shared cloud machine       | ✔️ (yes, but never exclusively)  | Everyone shares an environment (e.g. `beta`, `staging`) for development | Every time I've had this, I always have local development as well - and I lean into that because there's no fear of collisions of work.<br/><br/>Benefits tend to include being a downstream scrubbed replica of production more easily                                                                             |
| Production only            |                                  | Everyone shares the same production environment                         | I've thankfully never had to experience this. Very risky due to edits affecting people using application                                                                                                                                                                                                            |

[remote-vscode]: https://code.visualstudio.com/docs/remote/remote-overview
