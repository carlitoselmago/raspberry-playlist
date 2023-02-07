import glob, os
import random
from omxplayer import OMXPlayer
import time
from threading import Thread

class randomSeamlessVideos():

    #settings##################################

    seamless_gap=0.3 # time in seconds in wich we should launch the next video based on cpu delay. This needs to be fine tunned, speed might vary if runned from ssh or rc.local
    debug=True

    #end settings##############################

    vidfolder="videos"

    loaded_videos=[]
    videos=[]

    omxdargs="--no-osd --no-keys -b  --nohdmiclocksync"

    index=0
    queue_index=0
    current_video=0
    video_queue=3

    def __init__(self):

        #kill any left omx dbus process
        os.system("pkill -f omx")
        self.videos=glob.glob(self.vidfolder+"/*.mp4")

    def getRandomVideo(self,lastvideo=False):
        pickedvideo=random.choice(self.videos)
        if lastvideo:
            while pickedvideo==lastvideo:
                pickedvideo=random.choice(self.videos)
        return pickedvideo

    def loadNextVideo(self,index): #this will be runned as a thread

        videouri=self.getRandomVideo()
        self.echo("loading video",videouri,"on player index",self.queue_index)

        self.players[index].load(videouri)
        self.players[index].pause()
        self.index+=1
        self.queue_index+=1
        if self.queue_index>2:
            self.queue_index=0

    def unloadVideo(self):
        time.sleep(0.5)
        if len(self.loaded_videos)>1:
            todelete=self.loaded_videos.pop(0)
            todelete.quit()


    def playNext(self):
        self.echo("")
        #self.echo("Playing. Videos available on queue",self.loaded_videos)
        self.echo("Play next! with player index",self.current_video)

        if  isinstance(self.players[self.current_video],OMXPlayer):
            #self.loaded_videos[0].set_position(0.0)
            self.echo("Video available to play")
            self.echo(self.players[self.current_video].position())
            play=self.players[self.current_video].play()

            self.players[self.current_video].set_layer(self.index)
        else:
            #handle no videos to play
            self.echo("NO VIDEOS AVAILABLE TO PLAY!")
            pass


        #load next video
        start = time.time()
        #d = Thread(target=self.loadNextVideo)
        #d.start()
        next_index=self.current_video+1
        if next_index>2:
            next_index=0

        self.loadNextVideo(next_index)
        end = time.time()
        elapsed=(end-start)

        time.sleep(elapsed)
        shoulwait=True

        #handle the grey area of spected duration with the actual ending of the video
        while shoulwait:
            try:
                stat = self.players[self.current_video].playback_status()

                if  (self.players[self.current_video].duration()-self.players[self.current_video].position()) <= self.seamless_gap:
                    shouldwait=False
                    #end of video
                    self.nextVideo() #moves current_video index
                    break

            except Exception as e:
                self.echo(e)
                shouldwait=False
                break
                # presumably the video/audio playback ended. do what you need to do..
            time.sleep(0.0001)

    def nextVideo(self):
        self.current_video+=1
        if self.current_video==3:
            self.current_video=0

    def preloadQueue(self):
        self.echo("preloading Queue")
        self.echo( self.getRandomVideo())

        p1=OMXPlayer( self.getRandomVideo(),args=self.omxdargs)
        p1.pause()

        p2=OMXPlayer( self.getRandomVideo(),dbus_name='org.mpris.MediaPlayer2.omxplayer1',args=self.omxdargs)
        p2.pause()

        p3=OMXPlayer( self.getRandomVideo(),dbus_name='org.mpris.MediaPlayer2.omxplayer2',args=self.omxdargs)
        p3.pause()

        self.players=[
            p1,p2,p3
        ]
        for i in range(self.video_queue):
            self.echo("loading video",i)
            self.loadNextVideo(i)

    def startTheater(self):
        self.echo("theater start, preloading ",self.video_queue,"videos")
        start = time.time()
        self.preloadQueue()
        end = time.time()
        elapsed=(end-start)

        self.echo("preloaded took",elapsed," seconds")
        time.sleep(elapsed+2)
        while True:
            self.playNext()

    def echo(self,*arg):
        out=""
        if self.debug:
            for a in arg:
                out+=str(a)+" "
            print(out)


if __name__ == "__main__":
    RSV=randomSeamlessVideos()
    RSV.startTheater()
