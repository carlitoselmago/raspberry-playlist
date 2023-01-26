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

player = OMXPlayer( videos[0],"dbus_name='org.mpris.MediaPlayer2.omxplayer1")
player.pause()
#player.hide_video()
player2 = OMXPlayer( videos[1],"dbus_name='org.mpris.MediaPlayer2.omxplayer2")
player2.pause()
player2.hide_video()

sleep(player2.duration())
player2.pause()
player2.hide_video()
player.play()


"""
for v in videos:
    player = OMXPlayer( v)
    sleep(player.duration())
    #player1 = OMXPlayer( path + movie[1])
"""