from ....common.bash_utils import run_bash

def stats_linux_service_status(device_config, parameter):
    service = parameter.split(".")[1]
    return run_bash("systemctl is-active " + service, device_config).upper()