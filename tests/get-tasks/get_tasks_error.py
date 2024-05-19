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

    get_tasks = requests.get(base_url + 'tasks')

    if get_tasks.status_code != 200 and 'data' not in get_tasks.json():
        print("Test success")
    else:
        print("Test failed")
except:
    print("Test failed")