# vim:set ft=dockerfile:
FROM vertexproject/synapse:master

COPY storm-tutorial/ /storm-tutorial/
RUN ["python3", "-m", "synapse.tools.ingest", \
    "--verbose", "--core=sqlite:////storm-tutorial/sqlite-core.db", \
    "/storm-tutorial/ingest.json"]

ENTRYPOINT ["/bin/bash", "/storm-tutorial/entrypoint.sh"]
