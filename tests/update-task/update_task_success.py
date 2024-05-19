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

    uuid = get_tasks.json()['data'][0]['uuidTask']

    task = {
            'title': 'first task updated',
            'description': 'df',
            'preference': 2
        }    

    update = requests.put(base_url + f'tasks/{uuid}', headers=header, json=task)

    if update.status_code == 200 and update.json()["msg"] == "OK" and update.json()['data'] is not None:
        print("Test success")
    else:
        print("Test failed")
except:
    print("Test failed")
