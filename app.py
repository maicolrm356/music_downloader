import pandas as pd
import os
import yt_dlp as yt
import openpyxl
from openpyxl import load_workbook, Workbook
from openpyxl.utils import get_column_letter

excel = "./music.xlsx"
archivo = load_workbook(excel)
ruta_base = "C:/Users/maico/Music/music"
albums = []

def crear_carpetas_artistas(artista):
    # ruta_artista = f"{ruta_base}/{artista}"
    ruta_artista = os.path.join(ruta_base,artista)
    if not os.path.isdir(ruta_artista):
        try:    
            os.mkdir(ruta_artista)
            print(F"Se crea la carpeta del artista: {ruta_artista}")
        except:
            print("Error al crear la carpeta del album")
    else:
        print(f"Ya existe la carpeta del artista {ruta_artista}")

def crear_carpetas_de_albums(ruta_albums):
    if not os.path.isdir(ruta_albums):
        try:    
            os.makedirs(ruta_albums)
            print(F"Se crea la carpeta del album: {ruta_albums}")
        except:
            print("Error al crear la carpeta del album")
# path = 'C:/Users/maico/Music/music/Guns N Roses/Appetite For Destruction'
# ydl_opts = {
#     'ffmpeg_location': r'C:\Users\maico\Downloads\ffmpeg-2025-08-07-git-fa458c7243-essentials_build\ffmpeg-2025-08-07-git-fa458c7243-essentials_build\bin',
#     'format': 'm4a/bestaudio/best',
#     'outtmpl': f'{path}/%(track)s.%(ext)s',
#     # ℹ︝ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
#     'postprocessors': [
#         {  # Extract audio using ffmpeg
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'm4a',
#         },
#         {
#             'key': 'FFmpegMetadata',
#         }
#     ],
#     'retries': 10,             # más intentos
#     'fragment_retries': 10,    # más intentos por fragmento
#     'socket_timeout': 30,      # segundos de espera (por defecto es 10)
#     'http_chunk_size': 10485760,  # fuerza descargas en bloques de 10 MB                           
# }

# with yt.YoutubeDL(ydl_opts) as ydl:
#     error_code = ydl.download(URLS)
    
    


def obtener_artista_excel():
    nombres_hojas = archivo.sheetnames
    return nombres_hojas

def obtener_nombre_album(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'extract_flat': True,  # No intenta procesar cada video del playlist
        'force_generic_extractor': True,  # Evita usar extractores específicos que fallan
    }

    with yt.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            album_name = info.get('album') or info.get('playlist_title') or info.get('title')
            if album_name:
                album_name = album_name.replace("Album - ", "").strip()
            print(album_name)
            return album_name
        except Exception as e:
            print(f"⚠️ Error obteniendo nombre del álbum: {e}")
            return None

def descargar_albums(albums, artista):
    # path = 'C:/Users/maico/Music/music/Guns N Roses/Appetite For Destruction'
    # path = f"{ruta_base}/{artista}"
    # ydl_opts = {
    #     'ffmpeg_location': r'C:\Users\maico\Downloads\ffmpeg-2025-08-07-git-fa458c7243-essentials_build\ffmpeg-2025-08-07-git-fa458c7243-essentials_build\bin',
    #     'format': 'm4a/bestaudio/best',
    #     'outtmpl': f'{path}/%(track)s.%(ext)s',
    #     # ℹ︝ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    #     'postprocessors': [
    #         {  # Extract audio using ffmpeg
    #             'key': 'FFmpegExtractAudio',
    #             'preferredcodec': 'm4a',
    #         },
    #         {
    #             'key': 'FFmpegMetadata',
    #         }
    #     ],
    #     'retries': 10,             # más intentos
    #     'fragment_retries': 10,    # más intentos por fragmento
    #     'socket_timeout': 30,      # segundos de espera (por defecto es 10)
    #     'http_chunk_size': 10485760,  # fuerza descargas en bloques de 10 MB                           
    # }
    for album in albums:
        nombre_album = obtener_nombre_album(album)
        path = f"{ruta_base}/{artista}/{nombre_album}"
        crear_carpetas_de_albums(path)
        # print(path)

def obtener_albums():
    artistas = obtener_artista_excel()
    print(artistas)
    for artista in artistas:
        hoja_artista = archivo[artista]
        print("ARTISTA: " + artista)
        # crear_carpetas_artistas(artista)
        columnas = hoja_artista.max_column
        filas = hoja_artista.max_row

        for col in range(1, columnas +1):
            contador = 0
            for fila in range(1, filas + 1):
                celda = hoja_artista.cell(row=fila, column=col)
                link_album = celda.value
                if fila == 1:
                    albums.append(link_album)
                if link_album is not None:
                    contador += 1
        descargar_albums(albums,artista)
        albums.clear()
        # exit()
        # print(albums)

obtener_albums()

## HACER PRUEBAS DE DESCARGA


