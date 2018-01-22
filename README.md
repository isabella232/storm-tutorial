# Storm Tutorial
Storm is the query language used to interact with data in a Synapse hypergraph.
Storm allows you to ask about, retrieve, annotate, add, modify, and delete data from a Cortex.

This tutorial exists as an interactive Docker image. Visit
[Docker Installation Docs](https://docs.docker.com/engine/installation/#supported-platforms)
for instructions to install Docker.

Additional Storm documentation is available at:
[Storm Query Language - Basics](https://vertexprojectsynapse.readthedocs.io/en/latest/synapse/userguides/ug011_storm_basics.html).

### Getting Started
The following command starts the container and connects to the tutorial image.
```
$ docker run -it vertexproject/storm-tutorial:master
cli> help
ask  - Execute a query.
guid - Generate a new guid
help - List commands and display help output.
locs - List the current locals for a given CLI object
py   - Evaluate a line of python code with the cmd item.
quit - Quit the current command line interpreter.
cli>
```
