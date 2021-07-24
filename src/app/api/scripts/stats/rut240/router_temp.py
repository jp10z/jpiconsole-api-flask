from ....common.bash_utils import run_bash

def stats_rut240_router_temp(device_config):
    return int(run_bash("gsmctl --temp", device_config))/10