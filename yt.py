from pytube import YouTube
targetLink = input("Enter YouTube Link: ")
getLink = YouTube(targetLink)
print(getLink.title)
print(getLink.thumbnail_url)
allVideos = getLink.streams.all()
vid = list(enumerate(allVideos))
for i in vid:
  print(i)
print()
strm = int(input("Enter Video No: "))
allVideos[strm].download()
print("Download Successfully")
