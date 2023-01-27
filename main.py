import glob, os
import random
from omxplayer.player import OMXPlayer
import time

class randomSeamlessVideos():

    #settings##################################

    seamless_gap=0.2 # time in seconds in wich we should launch the next video based on cpu delay. This needs to be fine tunned, speed might vary if runned from ssh or rc.local

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
        self.loaded_videos.append(OMXPlayer( videouri,dbus_name='org.mpris.MediaPlayer2.omxplayer'+str(dbus),args='--no-osd --no-keys -b --nohdmiclocksync '))
        self.loaded_videos[-1].pause()
        #self.loaded_videos.append(player)


RSV=randomSeamlessVideos()

#play first video
RSV.loaded_videos[0].play()
time.sleep(RSV.loaded_videos[0].duration())
#video end, theres a second video loaded

i=3

while True:

    RSV.loaded_videos[-1].play()
    time.sleep(0.2) #this prevents a blank frame gap, giving time to play the next video before last gets deleted
    start = time.time()
    todelete=RSV.loaded_videos.pop(0)
    #load next video
    
    todelete.quit()
    RSV.loadNextVideo(i)
    end = time.time()
    elapsed=(end-start)
    time.sleep(RSV.loaded_videos[0].duration()-(2-elapsed)) #extra -2 seconds (+elapsed) to force the next fine tuning part
    shoulwait=True

    #handle the grey area of spected duration with the actual ending of the video 
    while shoulwait:
        try:
            stat = RSV.loaded_videos[0].playback_status()
          
            if  (RSV.loaded_videos[0].duration()-RSV.loaded_videos[0].position()) <= RSV.seamless_gap:
                shouldwait=False
                break
           
        except :
            shouldwait=False
            break
            # presumably the video/audio playback ended. do what you need to do..

    i+=1      
