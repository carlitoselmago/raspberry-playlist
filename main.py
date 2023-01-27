import glob, os
import random
from omxplayer.player import OMXPlayer
import time
import threading

class randomSeamlessVideos():

    #settings##################################

    playlist_length=10#75600 #based on 8'' average duration of each video

    #end settings##############################

    vidfolder="videos"

    loaded_videos=[]
    videos=[]    

    def __init__(self):

        #kill any left omx dbus process
        os.system("pkill -f omx")

        self.videos=glob.glob(self.vidfolder+"/*.mp4")

        #load first 2 videos
        self.loaded_videos.append(OMXPlayer(self.getRandomVideo(),dbus_name='org.mpris.MediaPlayer2.omxplayer'+str(1),args='--no-osd --no-keys -b'))
        self.loaded_videos[0].pause()
        self.loadNextVideo(2)


    def getRandomVideo(self,lastvideo=False):
        pickedvideo=random.choice(self.videos)
        if lastvideo:
            while pickedvideo==lastvideo:
                pickedvideo=random.choice(self.videos)
        return pickedvideo

    def loadNextVideo(self,i): #this will be runned as a thread
        dbus=1
        if (i % 2) == 0:
            #if even
            dbus=2
        #print("dbus",dbus)
        #get video uri
        videouri=self.getRandomVideo()
        self.loaded_videos.append(OMXPlayer( videouri,dbus_name='org.mpris.MediaPlayer2.omxplayer'+str(dbus),args='--no-osd --no-keys -b --nohdmiclocksync --refresh'))
        self.loaded_videos[-1].pause()
        #self.loaded_videos.append(player)



#if __name__ == "__main__":

RSV=randomSeamlessVideos()

#play first video
RSV.loaded_videos[0].play()
time.sleep(RSV.loaded_videos[0].duration())
#video end, theres a second video loaded
print("loaded",RSV.loaded_videos)

for i in range(3,160):
    #print("loop ",i)
    #remove finished video
    todelete=RSV.loaded_videos.pop(0)
    #play loaded and ready video 
    #print("loaded",RSV.loaded_videos)
    RSV.loaded_videos[-1].play()
    #load next video
    start = time.time()
    todelete.quit()
    #next_thread = threading.Thread(target=RSV.loadNextVideo, args=(i,))
    #next_thread.start()
    RSV.loadNextVideo(i)
    end = time.time()
    elapsed=(end-start)
    time.sleep(RSV.loaded_videos[0].duration()-(1-elapsed))



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
