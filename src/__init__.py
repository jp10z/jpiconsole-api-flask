from src.app import create_app
from src.app.common.config_controller import get_enviroment_host, get_enviroment_port, get_enviroment_debug, validate_config_file

def run():
    print("\nStarting API\n")

    enviroment_host = get_enviroment_host()
    enviroment_port = get_enviroment_port()
    enviroment_debug = get_enviroment_debug()

    if (
        str(enviroment_host).startswith("ERROR") == False and
        str(enviroment_debug).startswith("ERROR") == False and
        str(enviroment_port).startswith("ERROR") == False
    ):
        app = create_app()
        app.run(
            host=enviroment_host,
            port=enviroment_port,
            debug=enviroment_debug,
            use_reloader=False
        )
    else:
        print("enviroment_host -> " + enviroment_host)
        print("enviroment_port -> " + enviroment_port)
        print("enviroment_debug -> " + enviroment_debug)