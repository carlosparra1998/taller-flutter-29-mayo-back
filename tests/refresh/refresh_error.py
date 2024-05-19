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
    refresh=response.json()['data']['refresh_token']


    refresh_task = requests.post(base_url + "refresh", headers={
            'Authorization': f'Bearer {access}'})

    if refresh_task.status_code != 200 and refresh_task.json()["msg"] == "Only refresh tokens are allowed":
        print("Test success")
    else:
        print("Test failed")
except:
    print("Test failed")