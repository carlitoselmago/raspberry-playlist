import glob, os
import random
from omxplayer.player import OMXPlayer
from time import sleep

vidfolder="videos"

#settings##################################

playlist_length=10#75600 #based on 8'' average duration of each video

#end settings##############################

def get_random_video(lastvideo=False):
    pickedvideo=random.choice(videos)
    if lastvideo:
        while pickedvideo==lastvideo:
            pickedvideo=random.choice(videos)
    return pickedvideo

videos=glob.glob(vidfolder+"/*.mp4")

videosB=[]

for i,v in enumerate(videos):
    print("Loading video ",i)
    videosB.append(OMXPlayer( v,dbus_name='org.mpris.MediaPlayer2.omxplayer'+str(i),args='--no-osd --no-keys -b'))
    videosB[i].pause()

print("dbus pool ready")

"""
#pick a video to start have the var declared
pickedvideo=get_random_video()

print("Creating playlist...")
with open('playlist.m3u', 'w') as f:
    for i in range(playlist_length):
        pickedvideo=get_random_video(pickedvideo)
        f.write(pickedvideo+"\n")

print("Done, loading playlist and launching player")
"""
#execute player 
#os.system("vlc -I ncurses --video-on-top --fullscreen --loop --no-osd playlist.m3u")
