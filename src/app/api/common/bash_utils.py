from subprocess import Popen, PIPE

def run_bash(command, device_config):
    if device_config["connection"] == "local":
        session = Popen([
            "./src/app/api/common/script_controller.sh",
            command
        ], stdout=PIPE, stderr=PIPE)
        stdout, stderr = session.communicate()
        if stderr:
            return "ERROR: " + str(stderr)
        return stdout.decode('utf-8').replace("\n", "")
    elif device_config["connection"] == "ssh":
        session = Popen([
            "./src/app/api/common/script_controller.sh",
            "sshpass -p '" + device_config["password"] +
            "' ssh " +
            device_config["user"] +
            "@" +
            device_config["host"] +
            " '" +
            command +
            "'"
        ], stdout=PIPE, stderr=PIPE)
        stdout, stderr = session.communicate()
        if stderr:
            return "ERROR: " + str(stderr)
        return stdout.decode('utf-8').replace("\n", "")

def run_bash_bl(command, device_config):
    if device_config["connection"] == "local":
        session = Popen([
            "./src/app/api/common/script_controller.sh",
            command
        ], stdout=PIPE, stderr=PIPE)
        stdout, stderr = session.communicate()
        if stderr:
            return "ERROR: " + str(stderr)
        return stdout.decode('utf-8')
    elif device_config["connection"] == "ssh":
        session = Popen([
            "./src/app/api/common/script_controller.sh",
            "sshpass -p '" + device_config["password"] +
            "' ssh " +
            device_config["user"] +
            "@" +
            device_config["host"] +
            " '" +
            command +
            "'"
        ], stdout=PIPE, stderr=PIPE)
        stdout, stderr = session.communicate()
        if stderr:
            return "ERROR: " + str(stderr)
        return stdout.decode('utf-8')