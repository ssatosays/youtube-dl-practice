from __future__ import unicode_literals

import youtube_dl

music_list = [
    {'name': '君の体温', 'link': 'https://www.youtube.com/watch?v=QLsXgj4_gOc'}
]

def main():
    for music in music_list:
        name, link = music['name'], music['link']
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320'
            }],
            'outtmpl': f'download/{name}.%(ext)s'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            resp = ydl.download([link])
            assert resp == 0


if __name__ == "__main__":
    main()
