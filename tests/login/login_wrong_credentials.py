import requests
import json

try:
    base_url = 'http://35.224.111.41:5000/api/v1/'

    login_url = base_url + 'login'

    login_data = {
        'userName': 'usuario_prueba_wrong',
        'password': 'contraseña_prueba'
    }

    response = requests.post(login_url, json=login_data)

    if response.status_code != 200 and response.json()["msg"] == "Credenciales incorrectas":
        print("Test success")
    else:
        print("Test failed")
except:
    print("Test failed")
