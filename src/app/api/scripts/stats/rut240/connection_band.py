from ....common.bash_utils import run_bash

def stats_rut240_connection_band(device_config):
    result = run_bash("gsmctl --network", device_config)
    try:
        return result.split("\"")[5]
    except:
        return "ERROR"