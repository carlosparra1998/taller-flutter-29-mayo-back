import time as time
import requests

from tests.get_host import get_host

try:
    base_url = f"http://{get_host()}/api/v1/"

    register_url = base_url + 'register'

    register_data = {
        'userName': f'test_{time.time()}',
        'password': 'contrasena_prueba'
    }
    response = requests.post(register_url, json=register_data)

    if response.status_code == 200 and response.json()["msg"] == "OK":
        print("Test success")
    else:
        print("Test failed")
except:
    print("Test failed")