import ffmpeg

class VideoMaker:
    def __init__(self: object, background=None, audio=None) -> None:
        self.__background = background
        self.__audio = audio
    
    def set_background(self: object, file: str, image=True, video=False) -> None:
        self.__background = file

    def set_audio(self: object, file: str) -> None:
        self.__audio = file

    def save_video(self: object, filename: str, extension='mp4') -> None:
        file = f'{filename}.{extension}'

        input_still = ffmpeg.input(self.__background)
        input_audio = ffmpeg.input(self.__audio)

        out = ffmpeg.output(input_audio, input_still, file)
        out.run()
