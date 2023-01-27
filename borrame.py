import glob, os
import random
from omxplayer.player import OMXPlayer
from time import sleep
vidfolder="videos"

#settings##################################

playlist_length=10#75600 #based on 8'' average duration of each video

#end settings##############################

#kill any left omx dbus process
os.system("pkill -f omx")

def get_random_video(lastvideo=False):
    pickedvideo=random.choice(videos)
    if lastvideo:
        while pickedvideo==lastvideo:
            pickedvideo=random.choice(videos)
    return pickedvideo

videos=glob.glob(vidfolder+"/*.mp4")

player = OMXPlayer( videos[0],dbus_name='org.mpris.MediaPlayer2.omxplayer1',args='--no-osd --no-keys -b')
player.pause()
player2 = OMXPlayer( videos[1],dbus_name='org.mpris.MediaPlayer2.omxplayer2',args='--no-osd --no-keys -b')
sleep(player2.duration())

player.play()
player2 = OMXPlayer( videos[2],dbus_name='org.mpris.MediaPlayer2.omxplayer3',args='--no-osd --no-keys -b')
player2.pause()
sleep(player.duration())

player2.play()
"""
for v in videos:
    player = OMXPlayer( v)
    sleep(player.duration())
    #player1 = OMXPlayer( path + movie[1])
"""