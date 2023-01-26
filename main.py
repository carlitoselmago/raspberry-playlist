import glob, os
import random
from omxplayer.player import OMXPlayer
from time import sleep
import threading

vidfolder="videos"

#settings##################################

playlist_length=10#75600 #based on 8'' average duration of each video

#end settings##############################

def getRandomVideo(lastvideo=False):
    pickedvideo=random.choice(videos)
    if lastvideo:
        while pickedvideo==lastvideo:
            pickedvideo=random.choice(videos)
    return pickedvideo

def loadNextVideo(i): #this will be runned as a thread
    dbus=1
    if (i % 2) == 0:
        #if even
        dbus=2
    #get video uri
    videouri=getRandomVideo()
    player=OMXPlayer( videouri,dbus_name='org.mpris.MediaPlayer2.omxplayer'+str(dbus),args='--no-osd --no-keys -b') 
    player.pause()
    loaded_videos.append(player)

loaded_videos=[]
videos=glob.glob(vidfolder+"/*.mp4")

#load first 2 videos
loaded_videos.append(OMXPlayer(getRandomVideo(),dbus_name='org.mpris.MediaPlayer2.omxplayer'+str(1),args='--no-osd --no-keys -b'))
loadNextVideo(2)
#play first video
loaded_videos[0].play()
sleep(loaded_videos[0].duration())

#video end, theres a second video loaded
"""
for i in range(5):
    print("loop ",i)
    #remove finished video
    loaded_videos.pop(0)
    #play loaded and ready video 
    loaded_videos[0].play()
    #load next video
    next_thread = threading.Thread(target=loadNextVideo, args=(i,))
    next_thread.start()
    sleep(loaded_videos[0].duration())
"""


"""


def loadVideo():


def nextVideo(index,currentvideo=False):
    v=getRandomVideo()
    dbus=1
    if (index % 2) == 0:
        #if even
        dbus=2
    player=OMXPlayer( v,dbus_name='org.mpris.MediaPlayer2.omxplayer'+str(dbus),args='--no-osd --no-keys -b')    
    player.pause()
    return player


loaded_videos=[]
videos=glob.glob(vidfolder+"/*.mp4")

#video=getRandomVideo()

nextVideo(0)
"""
"""
for i in range(5):
    video=getRandomVideo(video)
    x = threading.Thread(target=nextVideo, args=(i,))
"""

"""
for i,v in enumerate(videos):
    print("Loading video ",i)
    videosB.append(OMXPlayer( v,dbus_name='org.mpris.MediaPlayer2.omxplayer'+str(i),args='--no-osd --no-keys -b'))
    videosB[i].pause()

print("dbus pool ready")
"""
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
