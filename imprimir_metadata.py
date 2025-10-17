import yt_dlp as yt

#gnr lies
url = 'https://music.youtube.com/playlist?list=OLAK5uy_loKqS03yOG47kKz8c6t_TQDvKtwFVCcwc'

with yt.YoutubeDL({'quiet': True}) as ydl:
    info = ydl.extract_info(url, download=False)

# Intentar obtener el nombre del álbum de distintas fuentes
album_name = info.get('album') or info.get('playlist_title') or info.get('title')

if album_name:
    album_name = album_name.replace("Album - ", "").strip()
print(album_name)
