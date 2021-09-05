from pytube import YouTube

url = 'Enter url'
my_video = YouTube(url)

print("**********Video Title***********")
#get Video Title
print(my_video.title)

print("*********Tumbnail Image*********")
#get Thumbnail Image
print(my_video.thumbnail_url)

print("*************Views**************")
#get no. of Views
print(my_video.views)

print("*************Length**************")
#get Length of video
print(my_video.length ,"seconds")

print("************Description***********")
#get Description
print(my_video.description)

print("**********Download video**********")
#get all the stream resolution for the video
#for stream in my_video.streams:
#    print(stream)

#set stream resolution
my_video = my_video.streams.get_highest_resolution()
#my_video = my_video.streams.get_by_itag(' ')

#Download video
my_video.download()
