import os
import sys
from moviepy import VideoFileClip

def convertir_a_mp3(ruta):
    """
    Convierte un video o los videos de una carpeta a MP3 extrayendo el audio.

    Args:
        ruta: La ruta al archivo de video o la carpeta que contiene los videos.
    """
    if os.path.isfile(ruta):
        # Si es un archivo, convertir a MP3
        nombre_archivo, _ = os.path.splitext(ruta)
        ruta_mp3 = nombre_archivo + ".mp3"
        convertir_video_a_mp3(ruta, ruta_mp3)
    elif os.path.isdir(ruta):
        # Si es un directorio, iterar sobre los archivos y convertir cada video
        for filename in os.listdir(ruta):
            if filename.endswith((".mp4", ".mov", ".avi")):  # Ajustar las extensiones según sea necesario
                ruta_video = os.path.join(ruta, filename)
                nombre_archivo, _ = os.path.splitext(filename)
                ruta_mp3 = os.path.join(ruta, nombre_archivo + ".mp3")
                convertir_video_a_mp3(ruta_video, ruta_mp3)
    else:
        print("Error: La ruta proporcionada no es un archivo ni un directorio.")

def convertir_video_a_mp3(ruta_video, ruta_mp3):
    """
    Convierte un solo video a MP3.

    Args:
        ruta_video: La ruta al archivo de video.
        ruta_mp3: La ruta donde se guardará el archivo MP3.
    """
    try:
        video = VideoFileClip(ruta_video)
        audio = video.audio
        audio.write_audiofile(ruta_mp3)
        print(f"Video convertido a MP3: {ruta_mp3}")
    except Exception as e:
        print(f"Error al convertir {ruta_video}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py <ruta_al_video_o_carpeta>")
        sys.exit(1)

    ruta = sys.argv[1]
    convertir_a_mp3(ruta)