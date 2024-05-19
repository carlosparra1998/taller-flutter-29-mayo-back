# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios (main.py, core/ y requirements.txt) al directorio de trabajo del contenedor
COPY ./project-back/main.py .
COPY ./project-back/core/ ./core
COPY ./project-back/requirements.txt .
COPY ./project-back/config/config.json .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que Flask se ejecutará dentro del contenedor (por defecto 5000)
EXPOSE 5000

# Comando para ejecutar la aplicación Flask cuando se inicie el contenedor
CMD ["python", "main.py"]
