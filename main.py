import pytube
import YouTube

url = 'url'
video = YouTube(url)
stream = video.streams.get_higest_resolution()

stream.download(output_path = 'E:/')