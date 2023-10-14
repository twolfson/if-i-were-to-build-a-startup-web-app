# Development Containment Analysis
**Winner: Language level, nothing else**

**Runner-up: OS level, with or without language level**

## Description
In addition to the [Development Machine](./development-machine.md), the application environment/dependencies can be contained and isolated

## Comparison
The choices aren't mutually exclusive, they can be combined as needed/wanted -- and some may be redundant with machine choice (e.g. virtual environments on a cloud machine)

<table>
    <tr>
        <th>Name</th> <th>Non-trivial previous experience?</th> <th>Description</th>
        <th>Notes</th>
    </tr>
    <tr>
        <td>No containment</td><td>✔️ (half of career-ish)</td><td>Nothing isolating dependencies on the machine</td>
        <td>
            This only happens with languages which use system-wide dependencies by default (e.g. Python and `pip`).
            <br/>
            <br/>
            It's risky if it's your local computer,
            because dependencies for unrelated things (e.g. your music player)
            may conflict with your application's ones
        </td>
    </tr>
    <tr>
        <td><strong>
            Language level (e.g.
                <a href="https://docs.python.org/3/library/venv.html#venv-def">Virtual Environments</a>,
                <a href="https://docs.npmjs.com/cli/v9/configuring-npm/folders">node_modules</a>
            ) (winner)
        </strong></td>
        <td>✔️ (majority)</td><td>Isolate dependencies through folders</td>
        <td>
            Provides sane isolation without concerns of something unrelated unexpectedly leading to conflict,
            <br/>
            as well as ability to easily inspect and adjust dependencies if needed (rare)
            <br/>
            <br/>
            For non-built-in (e.g. Virtual Environments), there's an extra lift of always invoking the shell wrapper
            (e.g. `bin/activate`) (unless shell auto-invokes) but OS level has similar drawbacks
        </td>
    </tr>
    <tr>
        <td>
            OS level (e.g.
                <a href="https://www.docker.com/">Docker</a>,
                <a href="https://www.vagrantup.com/">Vagrant</a>
            )
        </td>
        <td>✔️ (half of career-ish)</td><td>Isolate entire OS through either a container or full VM</td>
        <td>
            As close as possible to production environment,
            if not 1:1 due to using same solution in production.
            <br/>
            <br/>
            In practice, it's rare that an OS-specific issue is seen again in production
            (unless you develop on Windows and interface with paths)
            <br/>
            <br/>
            Drawbacks include needing to enter the container shell every time and deal with folder mounting/isolation
        </td>
    </tr>
</table>
