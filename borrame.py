import glob, os
import random
from omxplayer.player import OMXPlayer
from time import sleep
import time
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

#primeros dos ready
player = OMXPlayer( videos[0],dbus_name='org.mpris.MediaPlayer2.omxplayer1',args='--no-osd --no-keys -b')
player.pause()
player2 = OMXPlayer( videos[1],dbus_name='org.mpris.MediaPlayer2.omxplayer2',args='--no-osd --no-keys -b')
#reproduce player2
sleep(player2.duration()) #####

#reproduce player
player.play()

#mientras reproduce player1
start = time.time()
player2.quit()
player2 = OMXPlayer( videos[2],dbus_name='org.mpris.MediaPlayer2.omxplayer3',args='--no-osd --no-keys -b')
player2.pause() 
#player.exitEvent += lambda _, exit_code: player2.play()

end = time.time()
elapsed=(end-start)
#reproduce player1
print("times",player.duration(),elapsed)
sleep(player.duration()-elapsed) #####


player2.play()
start = time.time()
#mientras player2 reproduce, carga otro en dbus1
player = OMXPlayer( videos[4],dbus_name='org.mpris.MediaPlayer2.omxplayer1',args='--no-osd --no-keys -b')
player.pause()
end = time.time()
elapsed=(end-start)
sleep(player2.duration()-elapsed) #####

player.play()
sleep(player.duration())

"""
for v in videos:
    player = OMXPlayer( v)
    sleep(player.duration())
    #player1 = OMXPlayer( path + movie[1])
"""