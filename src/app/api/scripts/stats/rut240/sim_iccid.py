from ....common.bash_utils import run_bash

def stats_rut240_sim_iccid(device_config):
    return run_bash("gsmctl --iccid", device_config).upper()