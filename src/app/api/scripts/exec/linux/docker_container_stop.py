from ....common.bash_utils import run_bash

def exec_linux_docker_container_stop(device_config, parameter):
    docker_service = parameter.split(".")[1]
    return run_bash("docker stop " + docker_service, device_config)