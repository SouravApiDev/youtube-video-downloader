from pytube import YouTube
from google.colab import files
from IPython.display import Image
url = str(input("Youtube video url:- "))
yt = YouTube(url)
print(yt.title)
Image(yt.thumbnail_url, width=320, height=180)
video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

files.download(video)
