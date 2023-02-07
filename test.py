from omxplayer import OMXPlayer
from time import sleep
import glob, os

videos=glob.glob("videos/*.mp4")

stream1= videos[0]#'rtsp://10.0.5.170:554/stream'
stream2 = videos[1]#'rtsp://10.0.13.250:554/stream'
stream3 = videos[0]#'rtsp://10.0.17.212:554/stream'
stream4 = 'rtsp://10.0.8.133:554/stream'

player1 = OMXPlayer(stream1)
#player1.set_video_pos(0,0,960,540)

player2 = OMXPlayer(stream2, dbus_name='org.mpris.MediaPlayer2.omxplayer1')
#player2.set_video_pos(960,0,1920,540)

player3 = OMXPlayer(stream3, dbus_name='org.mpris.MediaPlayer2.omxplayer2')
#player3.set_video_pos(0,540,960,1080)

#player4 = OMXPlayer(stream4, dbus_name='org.mpris.MediaPlayer2.omxplayer3')
#player4.set_video_pos(960,540,1920,1080)
print("all loaded")
