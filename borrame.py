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

for v in videos:
    player = OMXPlayer( v)
    sleep(player.duration())
    #player1 = OMXPlayer( path + movie[1])