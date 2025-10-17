""" This module contains helper methods for connecting to and handling the CARLA server"""

import subprocess
import carla
from carla import Client

def launch_carla_server():
    # TODO: Replace with environment variable/make configurable
    subprocess.Popen(["/atlas/RSE/carla_server/CarlaUE4.sh", "-quality-level=Low"])

def connect_to_carla_server(address='localhost', port=2000, timeout=80.0):
    """ Connects to the carla server """
    client = carla.Client(address, port)
    client.set_timeout(timeout)
    return client
    