from ....common.bash_utils import run_bash

def exec_linux_docker_container_start(device_config, parameter):
    docker_service = parameter.split(".")[1]
    return run_bash("docker start " + docker_service, device_config)