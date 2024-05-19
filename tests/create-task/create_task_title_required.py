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

    task = {
            'description': 'df',
             #'color': self.color,
            'preference': 2
        }

    create_tasks = requests.post(base_url + 'tasks', json=task, headers=header)

    if create_tasks.status_code == 400 and 'data' not in create_tasks.json():
        print("Test success")
    else:
        print("Test failed")
except:
    print("Test failed")