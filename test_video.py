from video_maker import VideoMaker

vk = VideoMaker()
vk.set_background('outputs/image.jpg')
vk.set_audio('outputs/speech.mp3')
vk.save_video('outputs/teste')
