import os

def combinar_txts(ruta_carpeta, nombre_archivo_salida):
    with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
        for nombre_archivo in os.listdir(ruta_carpeta):
            if nombre_archivo.endswith('.txt'):
                ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo_entrada:
                    contenido = archivo_entrada.read()
                    archivo_salida.write(f"## {nombre_archivo}\n\n{contenido}\n\n\n\n")

combinar_txts('./dir_of_text_files/', 'output_file.txt')
