import requests
import json

from tests.get_host import get_host

try:
    base_url = f"http://{get_host()}/api/v1/"

    login_url = base_url + 'login'

    login_data = {
        'userName': 'user',
        'password': 'user'
    }

    response = requests.post(login_url, json=login_data)

    access = response.json()['data']['access_token']

    header = {'Authorization': f'Bearer {access}'}

    get_tasks = requests.get(base_url + 'tasks', headers=header)

    if get_tasks.status_code == 200 and get_tasks.json()["msg"] == "OK" and get_tasks.json()['data'] is not None:
        print("Test success")
    else:
        print("Test failed")
except:
    print("Test failed")
