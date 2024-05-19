import time as time
import requests

try:
    file = open("url.txt","rb")
    lines=list()
    for line in file.readlines():
            lines.append(line.rstrip().decode("utf-8"))
    file.close()  
    base_url = lines[0]
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