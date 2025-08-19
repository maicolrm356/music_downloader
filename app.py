import pandas as pd

import yt_dlp as yt

# prueba con los amantes sunt amentes
URLS = ['https://music.youtube.com/playlist?list=OLAK5uy_nhExNbsuT4shEKEVHqc_8VCjpfjJFT_lc']
# URLS = ['https://www.youtube.com/watch?v=oabjND9QW8Q&list=RD4QhFuJWqTAc&index=2']

path = 'C:/Users/maico/Music/music/Guns N Roses'
ydl_opts = {
    'ffmpeg_location': r'C:\Users\maico\Downloads\ffmpeg-2025-08-07-git-fa458c7243-essentials_build\ffmpeg-2025-08-07-git-fa458c7243-essentials_build\bin',
    'format': 'm4a/bestaudio/best',
    'outtmpl': f'{path}/%(track)s.%(ext)s',
    # ℹ︝ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [
        {  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            # 'preferredcodec': 'm4a',
            'preferredquality': '0',  # 0 = mejor calidad disponible
            'preferredcodec': 'wav',
        },
        {
            'key': 'FFmpegMetadata',
        }
    ]                                
}

with yt.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)