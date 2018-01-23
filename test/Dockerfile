FROM vertexproject/test-storm-tutorial:master

RUN mkdir -p /opt/test/
COPY test_storm_tutorial.py /opt/test/

WORKDIR /opt/test
ENTRYPOINT python -m unittest -v test_storm_tutorial
