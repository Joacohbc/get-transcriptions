import os
import sys
import whisper
import torch

torch.backends.cudnn.enabled = True

def transcribir_audio(ruta, modelo="base"):
    """
    Transcribe un audio o los audios de una carpeta a texto usando Whisper.
    Guarda cada transcripcion en un archivo .txt con el mismo nombre que el audio.

    Args:
        ruta: La ruta al archivo de audio o la carpeta que contiene los audios.
        modelo: El modelo de Whisper a utilizar (por defecto "base").
    """
    try:
        if os.path.isfile(ruta):
            # Si es un archivo, transcribir el audio
            transcribir_archivo_audio(ruta, modelo)
        elif os.path.isdir(ruta):
            # Si es un directorio, iterar sobre los archivos y transcribir cada audio
            for filename in os.listdir(ruta):
                if filename.endswith((".mp3", ".wav", ".ogg")):  # Ajustar las extensiones según sea necesario
                    ruta_audio = os.path.join(ruta, filename)
                    transcribir_archivo_audio(ruta_audio, modelo)
        else:
            print("Error: La ruta proporcionada no es un archivo ni un directorio.")
    except Exception as e:
        print(f"Error al transcribir: {e}")

def transcribir_archivo_audio(ruta_audio, modelo):
    """
    Transcribe un solo archivo de audio usando Whisper.
    Guarda la transcripcion en un archivo .txt con el mismo nombre que el audio.

    Args:
        ruta_audio: La ruta al archivo de audio.
        modelo: El modelo de Whisper a utilizar.
    """
    try:
        modelo = whisper.load_model(modelo)
        resultado = modelo.transcribe(ruta_audio)
        
        # Guardar la transcripcion en un archivo
        nombre_archivo, _ = os.path.splitext(ruta_audio)
        ruta_transcripcion = nombre_archivo + ".txt"
        with open(ruta_transcripcion, "w", encoding="utf-8") as f:
            f.write(resultado["text"])
        
        print(f"Transcripción de {ruta_audio} guardada en {ruta_transcripcion}")
    except Exception as e:
        print(f"Error al transcribir {ruta_audio}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py <ruta_al_audio_o_carpeta>")
        sys.exit(1)

    ruta = sys.argv[1]
    transcribir_audio(ruta)