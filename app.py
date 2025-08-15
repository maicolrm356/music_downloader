import pandas as pd

import yt_dlp as yt

URLS = ['https://www.youtube.com/watch?v=o1tj2zJ2Wvg&list=OLAK5uy_n13hmdsIozcCRyaY4cRDuuviphpfbzPrw']
# URLS = ['https://www.youtube.com/watch?v=oabjND9QW8Q&list=RD4QhFuJWqTAc&index=2']
path = 'C:/Users/maico/Music/music/Guns N Roses'
ydl_opts = {
    'ffmpeg_location': r'C:\Users\maico\Downloads\ffmpeg-2025-08-07-git-fa458c7243-essentials_build\ffmpeg-2025-08-07-git-fa458c7243-essentials_build\bin',
    'format': 'm4a/bestaudio/best',
    'outtmpl': f'{path}/%(title)s.%(ext)s',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [
        {  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        },
        {
            'key': 'FFmpegMetadata',
        }
    ]                                
}

with yt.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)