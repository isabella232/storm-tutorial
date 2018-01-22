# vim:set ft=dockerfile:
FROM vertexproject/synapse:v0.0.44

COPY storm-tutorial/ /storm-tutorial/
RUN ["python", "-m", "synapse.tools.ingest", \
    "--core=sqlite:////storm-tutorial/sqlite-core.db", \
    "/storm-tutorial/ingest.json"]

ENTRYPOINT ["/bin/bash", "/storm-tutorial/entrypoint.sh"]
