# Usar una imagen de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos requeridos
COPY youtube_transcript.py /app/
COPY requirements.txt /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar el script
CMD ["python", "youtube_transcript.py", "/app/urls.txt", "es"]
