# TODO LIST - BACK


## **Ejecución de los contenedores**

*$docker-compose up --build*

Es posible que en el primer intento no os funcione. Probad otra vez.

--

## **Ejecución de los test de ENDPOINTS**

1) Tener los contenedores activos
2) Acceder al directorio de tests/
3) Cambiar la configuración del fichero host adaptándolo a tus necesidades (host:port)
4) Ejecutar cada uno desde este directorio

Ejemplo: *$python register/register_success.py*

## **ENDPOINTS**

**Registro de usuario**

Endpoint: 
```
POST: /api/v1/register (no token required)
```

Input: 
```
{"userName" : "xxxx", "password" : "xxxxx"}
```

Output: 
```
{"msg": "OK", "data" : {}}
```

**Login**

Endpoint: 
```
POST: /api/v1/login (no token required)
```

Input: 
```
{"userName" : "xxxx", "password" : "xxxxx"}
```

Output: 
```
{"msg": "OK", "data" : {"access_token" : "xx", "refresh_token" : "xxx"}}
```

**Refresh**

Endpoint: 
```
POST: /api/v1/refresh (refresh token required)
```

Output: 
```
{"msg": "OK", "data" : {"access_token" : "xx", "refresh_token" : "xxx"}}
```

**Obtener todas las tareas del usuario**

Endpoint: 
```
GET: /api/v1/tasks (token required)
```

Output: 
```
{"msg" : "OK", "data" : [{tarea 1}, {tarea 2}, ..., {tarea n}]}
```

**Crear una tarea**

Endpoint: 
```
POST: /api/v1/tasks (token required)
```

Input: 
```
{"title": "first task 232", "description": "df", "color": "blue", "preference": 2}
```

Output: 
```
{"msg" : "OK", "data" : {tarea creada}}
```

**Modificar una tarea**

Endpoint: 
```
PUT: /api/v1/tasks/<uuid:uuidTask> (token required)
```

Input: 
```
{"title": "first task 232", "description": "df", "color": "blue", "preference": 2}
```

Output: 
```
{"msg" : "OK", "data" : {tarea modificada}}
```

**Borrar una tarea**

Endpoint: 
```
DELETE: /api/v1/tasks/<uuid:uuidTask> (token required)
```

Output: 
```
{"msg" : "OK", "data" : {}}
```
