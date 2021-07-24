from ....common.bash_utils import run_bash

def stats_rut240_connection_status(device_config):
    return run_bash("gsmctl --connstate", device_config)