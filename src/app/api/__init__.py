from flask import Blueprint, request, jsonify
from ..common.config_controller import get_device_config

api = Blueprint('api', __name__, url_prefix='/api')

## import scripts status linux

from .scripts.stats.linux.lsb_release import *
from .scripts.stats.linux.kernel import *
from .scripts.stats.linux.uptime import *
from .scripts.stats.linux.cpu_temp import *
from .scripts.stats.linux.ip import *
from .scripts.stats.linux.service_status import *
from .scripts.stats.linux.docker_container_status import *
from .scripts.stats.linux.usb_kname import *
from .scripts.stats.linux.usb_mount import *
from .scripts.stats.linux.usb_size_total import *
from .scripts.stats.linux.usb_size_free import *
from .scripts.stats.linux.usb_size_used import *
from .scripts.stats.linux.usb_size_used_percent import *
from .scripts.stats.linux.smb_status import *

## import scripts status rut240

from .scripts.stats.rut240.sim_status import *
from .scripts.stats.rut240.sim_iccid import *
from .scripts.stats.rut240.router_temp import *
from .scripts.stats.rut240.connection_status import *
from .scripts.stats.rut240.connection_link import *
from .scripts.stats.rut240.connection_band import *
from .scripts.stats.rut240.sms_list import *

## import scripts exec linux

from .scripts.exec.linux.usb_umount import *
from .scripts.exec.linux.usb_mount import *
from .scripts.exec.linux.smb_umount import *
from .scripts.exec.linux.smb_mount import *
from .scripts.exec.linux.service_start import *
from .scripts.exec.linux.service_stop import *
from .scripts.exec.linux.docker_container_start import *
from .scripts.exec.linux.docker_container_stop import *

## STAT API Method

@api.route('/stats', methods=['POST'])
def api_stats():
    return controller("stats", request.json)

## EXEC API Method

@api.route('/exec', methods=['POST'])
def api_exec():
    return controller("exec", request.json)

## CONTROLLER

def controller(method, request):
    ## Validate if request exists
    if request is None:
        return jsonify("ERROR: None request"), 400
    # Validate device_id
    try:
        device_id = request["device_id"]
    except:
        return jsonify("ERROR: device_id invalid"), 400
    # Get device config from json and continue
    device_config = get_device_config(device_id)
    if str(device_config).startswith("ERROR:") == False:
        # Prepare function header
        orig_method = method
        method = method + "_" + device_config["type"]
        # Validate is parameters exists in request
        try:
            request["parameters"]
        except:
            return jsonify("ERROR: parameters not found"), 400
        # Create context with parameters to return
        context = {}
        for parameter in request["parameters"]:
            # Validate parameter scheme
            try:
                parameter["parameter"]
            except:
                return jsonify("ERROR: invalid parameters scheme"), 400
            try:
                # Execute if parameters without sub-parameters
                if len(parameter["parameter"].split(".")) == 1:
                    func = globals()[method + "_" + parameter["parameter"]]
                    result = func(device_config)
                # Execute if parameters with sub-parameters
                else:
                    func = globals()[method + "_" + parameter["parameter"].split(".")[0]]
                    result = func(device_config, parameter["parameter"])
                # In case if functions returns empty result
                if orig_method == "exec" and result.replace("\n", "") == "":
                    result = "done"
                # Set function response in context
                context[parameter["parameter"]] = result
            # In case of exception
            except Exception as e:
                print("Error: " + str(e))
                if "takes 1 positional argument" in str(e):
                    context[parameter["parameter"]] = "ERROR: invalid parameters"
                elif "object has no attribute" in str(e):
                    context[str(parameter["parameter"])] = "ERROR: invalid parameter"
                else:
                    context[parameter["parameter"]] = "ERROR: parameter does not exists"
    else:
        return jsonify(device_config), 400
    return jsonify(context)