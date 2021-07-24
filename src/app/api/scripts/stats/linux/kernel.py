from ....common.bash_utils import run_bash

def stats_linux_kernel(device_config):
    return run_bash("uname", device_config) + " " + run_bash("uname -r", device_config)