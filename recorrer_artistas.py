import json
import pandas as pd
import os
import yt_dlp as yt
import openpyxl
from openpyxl import load_workbook, Workbook
from openpyxl.utils import get_column_letter
from mutagen.easyid3 import EasyID3

data = json.load(open("all_music.json"))

ruta_base = "/home/michael/Música/mi musica"
ruta_descarga = "/home/michael/Música/mi musica"

config_obtener_nombre_album = {
        'quiet': True,
        'skip_download': True,
        'extract_flat': True,  # No intenta procesar cada video del playlist
        'force_generic_extractor': True,  # Evita usar extractores específicos que fallan
    }


def obtener_nombre_album(url):
    ydl_opts = config_obtener_nombre_album
    with yt.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            album_name = info.get('album') or info.get('playlist_title') or info.get('title')
            if album_name:
                album_name = album_name.replace("Album - ", "").strip()
            if "/" in album_name:
                album_name = album_name.replace("/", "-").strip()
            print(album_name)
            return album_name
        except Exception as e:
            print(f"⚠️ Error obteniendo nombre del álbum: {e}")
            return None

def crear_carpetas_de_albums(ruta_albums):
    if not os.path.isdir(ruta_albums):
        try:    
            os.makedirs(ruta_albums)
            print(F"Se crea la carpeta del album: {ruta_albums}")
            return True
        except:
            print("Error al crear la carpeta del album")
    else: 
        print(f"Ya existe la carpeta del album: {ruta_albums}")

for artista in data["artistas"]:
    print(f"Artista: {artista['nombre']}")
    artist = artista['nombre']
    for link in artista["albums"]:
        nombre_album = obtener_nombre_album(link)
        path = f"{ruta_base}/{artist}/{nombre_album}"
        
        if crear_carpetas_de_albums(path):
            print(path)
            ydl_opts = {
                'ffmpeg_location': r'/usr/bin/ffmpeg',

                #'ffmpeg_location': r'C:\Users\maico\Downloads\ffmpeg-2025-08-07-git-fa458c7243-essentials_build\ffmpeg-2025-08-07-git-fa458c7243-essentials_build\bin',
                'format': 'bestaudio/best',
                'outtmpl': f'{path}/%(track)s.%(ext)s',
                # ℹ︝ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
                #'cookiesfrombrowser': (
                #        'brave',
                #        '/home/michael/snap/brave/current/.config/BraveSoftware/Brave-Browser',
                #        None,
                #        'Default'
                #    ),
                'postprocessors': [
                    {  # Extract audio using ffmpeg
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                    },
                    {
                        'key': 'FFmpegMetadata',
                    }
                ],
                
                #'cookiefile': 'cookies.txt',
                #'js_runtimes': {
                 #   'node': {
                  #      'path': '/usr/bin/node'
                   # }
                #},

                'extractor_args': {
                    'youtube': {
                        'player_client': ['android']
                    }
                },
                
                'remote_components': ['ejs:github'],
                'retries': 30,             # más intentos
                'fragment_retries': 30,    # más intentos por fragmento
                'socket_timeout': 30,      # segundos de espera (por defecto es 10)
                'http_chunk_size': 10485760,  # fuerza descargas en bloques de 10 MB                           
                'ignoreerrors': True,
                'noplaylist': False,
                'extract_flat': False,
            }
            
            # Descargar las canciones
            with yt.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=True)
            
            # Procesar metadatos de las canciones descargadas
            entries = info.get("entries", [info])
            for index, entry in enumerate(entries, start=1):
                title = entry.get("title", "Desconocido")
                artist = entry.get("artist") or entry.get("uploader", "Desconocido")
                album = entry.get("album") or info.get("title", "Álbum desconocido")
                track_number = entry.get("track_number") or index  # si no lo trae, usa el orden

                # Ruta del archivo descargado
                filename = os.path.join(path, f"{title}.mp3")

                if os.path.exists(filename):
                    try:
                        audio = EasyID3(filename)
                    except Exception:
                        audio = EasyID3()
                    
                    audio["title"] = title
                    audio["artist"] = artist
                    audio["album"] = album
                    audio["tracknumber"] = str(track_number)
                    audio.save(filename)
                    print(f"🎵 Etiquetas actualizadas: {title} (Track {track_number})")
                else:
                    print(f"⚠️ No se encontró el archivo: {filename}")