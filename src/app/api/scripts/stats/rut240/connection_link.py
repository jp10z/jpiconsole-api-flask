from ....common.bash_utils import run_bash

def stats_rut240_connection_link(device_config):
    return run_bash("gsmctl --netstate", device_config)