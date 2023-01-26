import vlc, time

instance = vlc.Instance("--aout=alsa")
player = instance.media_player_new()
video = instance.media_new("videos/clip001.mp4")
player.set_media(video)

player.play()
time.sleep(10)
player.stop()