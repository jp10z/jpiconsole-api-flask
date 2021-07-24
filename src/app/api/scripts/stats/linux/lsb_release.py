from ....common.bash_utils import run_bash

def stats_linux_lsb_release(device_config):
    return run_bash("lsb_release -si", device_config) + " " + run_bash("lsb_release -sr", device_config)