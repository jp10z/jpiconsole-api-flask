from src.app import create_app
from src.app.common.config_controller import get_enviroment_host, get_enviroment_port, get_enviroment_debug

def run():
    enviroment_host = get_enviroment_host()
    enviroment_port = get_enviroment_port()
    enviroment_debug = get_enviroment_debug()

    app = create_app()
    app.run(
        host=enviroment_host,
        port=enviroment_port,
        debug=enviroment_debug,
        use_reloader=False
    )