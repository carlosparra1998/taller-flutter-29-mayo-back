import time
import requests
import json

import sys, os
sys.path.append(os.path.abspath('../'))
from tests.get_host_util import get_host

try:
    base_url = f"http://{get_host()}/api/v1/"

    register_url = base_url + 'register'

    register_data = {
        'userName': 'user',
        'password': 'user'
    }
    requests.post(base_url + "register", json=register_data)

    response = requests.post(register_url, json=register_data)

    if response.status_code != 200 and response.json()["msg"] == "El usuario ya existe":
        print("Test success")
    else:
        print("Test failed")
except:
    print("Test failed")

