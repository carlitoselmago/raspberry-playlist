import glob, os
import random
vidfolder="videos"

#settings##################################

playlist_length=75600 #based on 8'' average duration of each video

#end settings##############################

def get_random_video(lastvideo=False):
    pickedvideo=random.choice(videos)
    if lastvideo:
        while pickedvideo==lastvideo:
            pickedvideo=random.choice(videos)
    return pickedvideo

videos=glob.glob(vidfolder+"/*.mp4")

#pick a video to start have the var declared
pickedvideo=get_random_video()

print("Creating playlist...")
with open('playlist.m3u', 'w') as f:
    for i in range(playlist_length):
        pickedvideo=get_random_video(pickedvideo)
        f.write(pickedvideo+"\n")

print("Done, loading playlist and launching player")
#execute player 
os.system("cvlc --video-on-top --fullscreen --loop --no-osd playlist.m3u")
