Storm Tutorial
=======

|dockerhub|_ |synvers|_

Storm is the query language used to interact with data in a Synapse hypergraph.
Storm allows you to ask about, retrieve, annotate, add, modify, and delete data from a Cortex.

This tutorial exists as an interactive Docker image.
Visit https://docs.docker.com/engine/installation/#supported-platforms for instructions to install Docker.

Additional Storm documentation is available at https://vertexprojectsynapse.readthedocs.io/en/latest/synapse/userguides/ug011_storm_basics.html.

Getting Started
------------

The following command starts the container and connects to the tutorial image.

.. parsed-literal::
  $ docker run -it vertexproject/storm-tutorial:master
  cli> help
  ask  - Execute a query.
  guid - Generate a new guid
  help - List commands and display help output.
  locs - List the current locals for a given CLI object
  py   - Evaluate a line of python code with the cmd item.
  quit - Quit the current command line interpreter.
  cli>

.. |dockerhub| image:: https://img.shields.io/docker/build/vertexproject/storm-tutorial.svg?branch=master
.. _dockerhub: https://hub.docker.com/r/vertexproject/storm-tutorial/

.. |synvers| image:: https://img.shields.io/badge/synapse-v0.0.44-green.svg 
.. _synvers: https://github.com/vertexproject/synapse
