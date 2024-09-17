# YouTube Transcript Downloader

Este proyecto proporciona una herramienta en Python que descarga transcripciones de videos de YouTube sin utilizar un API Token. Utiliza la librería `youtube-transcript-api` para obtener las transcripciones en el idioma que especifiques y las guarda en archivos de texto, uno por video. Además, la aplicación está dockerizada para facilitar su ejecución en cualquier entorno.

## Características

- Descarga transcripciones de videos de YouTube sin necesidad de usar un API Token.
- Guarda cada transcripción en un archivo `.txt` con el nombre del video.
- Admite especificar el idioma de la transcripción.
- Dockerizado para fácil ejecución y portabilidad.

## Requisitos

- [Python 3.9 o superior](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/youtube-transcriber.git
    cd youtube-transcriber
    ```

2. Instala las dependencias (opcional si no utilizas Docker):

    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Sin Docker

1. Crea un archivo `urls.txt` con las URLs de los videos de YouTube, una por línea.

2. Ejecuta el script de Python:

    ```bash
    python youtube_transcript.py urls.txt [idioma]
    ```

    - El parámetro `idioma` es opcional (por defecto es `en` para inglés). Ejemplo para español: `es`.

3. Las transcripciones se guardarán en archivos `.txt` con el nombre del video en la misma carpeta.

### Con Docker

1. Asegúrate de tener un archivo `urls.txt` en tu carpeta actual con las URLs de los videos.

2. Construye la imagen de Docker:

    ```bash
    docker build -t youtube-transcriber .
    ```

3. Ejecuta el contenedor y monta el directorio actual para que las transcripciones se guarden en tu máquina local:

    ```bash
    docker run -v $(pwd):/app youtube-transcriber
    ```

    - Las transcripciones se guardarán en tu carpeta local en archivos `.txt` con el nombre del video.

## Ejemplo de `urls.txt`

    ```
    https://www.youtube.com/watch?v=dQw4w9WgXcQ
    https://www.youtube.com/watch?v=9bZkp7q19f0
    ```

## Notas

- El script no funcionará con videos que no tengan transcripciones automáticas o manuales habilitadas.
- Si el video tiene varias transcripciones en diferentes idiomas, puedes especificar el idioma deseado usando el código ISO del idioma (por ejemplo, `en` para inglés, `es` para español, `fr` para francés, etc.).