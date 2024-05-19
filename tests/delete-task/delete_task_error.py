import requests
import json

try:
    base_url = 'http://35.224.111.41:5000/api/v1/'

    login_url = base_url + 'login'

    login_data = {
        'userName': 'user',
        'password': 'user'
    }

    response = requests.post(login_url, json=login_data)

    access = response.json()['data']['access_token']

    header = {'Authorization': f'Bearer {access}'}

    task = {
            'title': 'first task 232',
            'description': 'df',
             #'color': self.color,
            'preference': 2
        }

    create_tasks = requests.post(base_url + 'tasks', json=task, headers=header)

    task_uuid = create_tasks.json()['data']['uuidTask'] + "WILLNOTEXIST"

    delete = requests.delete(base_url + f'tasks/{task_uuid}', headers=header)

    if delete.status_code != 200:
        print("Test success")
    else:
        print("Test failed")
except:
    print("Test failed")