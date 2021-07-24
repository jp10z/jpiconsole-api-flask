from ....common.bash_utils import run_bash

def stats_rut240_sim_status(device_config):
    return run_bash("gsmctl --simstate", device_config)