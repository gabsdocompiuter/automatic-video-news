from moviepy.editor import *
import util


class VideoMaker:
    def __init__(self: object) -> None:
        self.__clips = []

    def create_clip(
        self: object,
        image_filename: str,
        audio_filename: str,
    ):
        audio_clip = AudioFileClip(audio_filename)
        clip = ImageClip(image_filename)

        clip.audio = audio_clip
        clip.duration = audio_clip.duration
        clip.fps = 24

        self.__clips.append(clip)

    def save_video(self: object, filename: str, extension='mp4') -> None:
        file = util.filename(filename, extension)

        video = concatenate_videoclips(self.__clips)
        video.write_videofile(file)
