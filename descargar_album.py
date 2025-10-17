import yt_dlp as yt

URLS = 'https://music.youtube.com/playlist?list=OLAK5uy_loKqS03yOG47kKz8c6t_TQDvKtwFVCcwc'
path = 'C:/Users/maico/Music/music/Guns N Roses/arroz con leche'
ydl_opts = {
    'ffmpeg_location': r'C:\Users\maico\Downloads\ffmpeg-2025-08-07-git-fa458c7243-essentials_build\ffmpeg-2025-08-07-git-fa458c7243-essentials_build\bin',
    'format': 'm4a/bestaudio/best',
    'outtmpl': f'{path}/%(track)s.%(ext)s',
    # ℹ︝ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [
        {  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        },
        {
            'key': 'FFmpegMetadata',
        }
    ],
    'retries': 10,             # más intentos
    'fragment_retries': 10,    # más intentos por fragmento
    'socket_timeout': 30,      # segundos de espera (por defecto es 10)
    'http_chunk_size': 10485760,  # fuerza descargas en bloques de 10 MB                           
}

with yt.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)
    