# import yt_dlp as yt

# URLS = 'https://music.youtube.com/playlist?list=OLAK5uy_loKqS03yOG47kKz8c6t_TQDvKtwFVCcwc'
# path = 'C:/Users/maico/Music/music/PXNDX/Arroz Con Leche (Collectors Edition)'
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
    
#     # # ✅ Agrega el número de pista (orden del álbum) dentro de la metadata
#     'postprocessor_args': [
#         '-metadata', 'track=%(playlist_index)s'
#     ],

#     'retries': 20,             # más intentos
#     'fragment_retries': 20,    # más intentos por fragmento
#     'socket_timeout': 30,      # segundos de espera (por defecto es 10)
#     'http_chunk_size': 10485760,  # fuerza descargas en bloques de 10 MB                           
# }

# with yt.YoutubeDL(ydl_opts) as ydl:
#     error_code = ydl.download(URLS)
    
import os
import yt_dlp as yt
from mutagen.easyid3 import EasyID3

# URL del álbum o playlist
URL = "https://music.youtube.com/playlist?list=OLAK5uy_ltQiuNnoBifeiEYSjm5Ac1Z-x3ydiYrq4"
URL = "https://music.youtube.com/playlist?list=OLAK5uy_lBFwKbOYWuj1MjWRuUGTiVc1Y58Jaa8Sw"

# Carpeta de salida
OUTPUT_DIR = "C:/Users/maico/Music/music/Guns N' Roses/Appetite For Destruction"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Configuración base de descarga
ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": os.path.join(OUTPUT_DIR, "%(title)s.%(ext)s"),
    "postprocessors": [
        {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"},
    ],
    "quiet": False,
}

# Descargar las canciones
with yt.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=True)

# Procesar metadatos de las canciones descargadas
entries = info.get("entries", [info])
for index, entry in enumerate(entries, start=1):
    title = entry.get("title", "Desconocido")
    artist = entry.get("artist") or entry.get("uploader", "Desconocido")
    album = entry.get("album") or info.get("title", "Álbum desconocido")
    track_number = entry.get("track_number") or index  # si no lo trae, usa el orden

    # Ruta del archivo descargado
    filename = os.path.join(OUTPUT_DIR, f"{title}.mp3")

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

# def obtener_nombre_artista(url):
#     ydl_opts = {
#         'quiet': True,
#         'skip_download': True,
#         'extract_flat': True,
#         'force_generic_extractor': True,
#     }

#     with yt.YoutubeDL(ydl_opts) as ydl:
#         try:
#             info = ydl.extract_info(url, download=False)
            
#             # 🔍 Intenta varias claves donde puede venir el nombre del artista
#             artista = (
#                 info.get('artist') or
#                 info.get('uploader') or
#                 info.get('channel') or
#                 info.get('uploader_id')
#             )
            
#             # Si no lo encontró en el nivel superior, intenta dentro del primer track
#             if not artista and 'entries' in info and info['entries']:
#                 primer_track = info['entries'][0]
#                 artista = (
#                     primer_track.get('artist') or
#                     primer_track.get('uploader') or
#                     primer_track.get('channel')
#                 )

#             if artista:
#                 artista = artista.strip()

#             print(f"🎤 Artista: {artista}")
#             return artista

#         except Exception as e:
#             print(f"⚠️ Error obteniendo artista: {e}")
#             return None

# obtener_nombre_artista(URL)