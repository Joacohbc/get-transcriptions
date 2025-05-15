import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import urllib.request
import sys

def get_video_title(video_url):
    """Obtiene el título del video de YouTube."""
    try:
        html = urllib.request.urlopen(video_url).read().decode('utf-8')
        title_start = html.find('<title>') + len('<title>')
        title_end = html.find('</title>')
        return html[title_start:title_end].replace(' - YouTube', '').strip().replace('/', '-')
    except Exception as e:
        print(f"Error al obtener el título del video: {e}")
        return "untitled"

def get_video_id(video_url):
    """Extrae el ID del video de YouTube."""
    return video_url.split("v=")[1].split("&")[0]

def download_transcripts(urls_file, language="en"):
    """Descarga transcripciones de los videos en las URLs proporcionadas."""
    with open(urls_file, 'r') as file:
        video_urls = file.readlines()

    formatter = TextFormatter()
    
    # Asegurar que el directorio de transcripciones exista
    os.makedirs(os.path.join(os.getcwd(), 'transcripts'), exist_ok=True)

    for url in video_urls:
        url = url.strip()
        if not url:
            continue

        try:
            video_id = get_video_id(url)
            print(f"Descargando transcripción para el video ID: {video_id}")
            
            # Obtener la transcripción
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
            
            if not transcript:
                print(f"No se encontró transcripción para {url}")
                continue
                
            try:
                # Formatear la transcripción en texto sin marcas de tiempo
                formatted_transcript = formatter.format_transcript(transcript)
                
                # Obtener el título del video para usarlo como nombre de archivo
                title = get_video_title(url)
                filename = f"{title}.txt"
                
                # Guardar la transcripción en el directorio de transcripciones
                filepath = os.path.join(os.getcwd(), 'transcripts', filename)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(formatted_transcript)
                print(f"Transcripción guardada en: {filepath}")
                
            except AttributeError:
                # Manejo específico para el error 'dict' object has no attribute 'text'
                print(f"Error al formatear la transcripción de {url}. Usando método alternativo...")
                
                # Método alternativo: extraer manualmente el texto de cada segmento
                text_content = "\n".join([entry.get('text', '') for entry in transcript])
                
                # Obtener el título del video para usarlo como nombre de archivo
                title = get_video_title(url)
                filename = f"{title}.txt"
                
                # Guardar la transcripción en el directorio de transcripciones
                filepath = os.path.join(os.getcwd(), 'transcripts', filename)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(text_content)
                print(f"Transcripción guardada usando método alternativo en: {filepath}")

        except Exception as e:
            print(f"Error al obtener la transcripción de {url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python youtube_transcript.py <archivo_urls.txt> [idioma]")
    else:
        urls_file = sys.argv[1]
        language = sys.argv[2] if len(sys.argv) > 2 else "en"
        download_transcripts(urls_file, language)
