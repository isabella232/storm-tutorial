#!/bin/bash
nohup python -m synapse.tools.dmon /storm-tutorial/dmon.json &>/dev/null &
sleep 2
python -m synapse.tools.cmdr tcp://127.0.0.1:47322/core
