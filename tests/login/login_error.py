import requests
import json

from tests.get_host import get_host

try:
    base_url = f"http://{get_host()}/api/v1/"

    login_url = base_url + 'login'

    login_data = {
        'password': 'contraseña_prueba'
    }

    response = requests.post(login_url, json=login_data)

    if response.status_code != 200 and response.json()["msg"] == "Ha fallado el proceso":
        print("Test success")
    else:
        print("Test failed")
except:
    print("Test failed")


