from ....common.bash_utils import run_bash, run_bash_bl
import json

def stats_linux_docker_container_status(device_config, parameter):
    service = parameter.split(".")[1]
    result = run_bash("docker inspect --format=\"{{json .State.Status}}\" " + service, device_config).replace("\"", "").upper()
    if "CANNOT CONNECT TO THE DOCKER DAEMON" in result:
        result = "DOCKER OFF"
    elif "NO SUCH OBJECT" in result:
        result = "NOT FOUND"
    return result