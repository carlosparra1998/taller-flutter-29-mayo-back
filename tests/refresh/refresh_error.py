import requests
import json

import sys, os
sys.path.append(os.path.abspath('../'))
from tests.get_host_util import get_host

try:
    base_url = f"http://{get_host()}/api/v1/"

    login_url = base_url + 'login'

    login_data = {
        'userName': 'user',
        'password': 'user'
    }
    
    requests.post(base_url + "register", json=login_data)

    response = requests.post(login_url, json=login_data)

    access = response.json()['data']['access_token']
    refresh=response.json()['data']['refresh_token']


    refresh_task = requests.post(base_url + "refresh", headers={
            'Authorization': f'Bearer {access}'})

    if refresh_task.status_code != 200 and refresh_task.json()["msg"] == "Only refresh tokens are allowed":
        print("Test success")
    else:
        print("Test failed")
except:
    print("Test failed")