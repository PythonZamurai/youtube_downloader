from pytube import YouTube

download_link = input('動画のURLを入力:')
video = YouTube(download_link)
youtube_stream = video.streams.get_highest_resolution()

print('ダウンロード中...')
youtube_stream.download()
print(f'{video.title}のダウンロードが完了しました。')