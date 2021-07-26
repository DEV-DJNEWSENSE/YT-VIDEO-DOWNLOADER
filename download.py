from pytube import YouTube
link = input("enter video url ;) ")
yt = YouTube(link)
videos = yt.streams.all()
video = list(enumerate(videos))
for i in video:
    print(i)

print("enter the desired format \n 144 \n 240 \n 360 \n 720 \n 1080 \n 1440 \n 2160")
dn_option = int(input("enter the option : "))
dn_video = videos[dn_option]
dn_video.download()
print("download successfully")
