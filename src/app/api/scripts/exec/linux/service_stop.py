from ....common.bash_utils import run_bash

def exec_linux_service_stop(device_config, parameter):
    service = parameter.split(".")[1]
    return run_bash("sudo systemctl stop " + service, device_config)