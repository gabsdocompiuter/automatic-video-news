from moviepy.editor import *


def create_clip(name: str) -> ImageClip:
    audio_clip = AudioFileClip(f'{name}.mp3')
    clip = ImageClip(f'{name}.jpg')

    clip.audio = audio_clip
    clip.duration = audio_clip.duration
    clip.fps = 24

    return clip


def main():
    clips = []

    clips.append(create_clip(
        'temp/bloqueio-da-ponte-do-fandango-suspende-aulas-em-cinco-escolas'))

    clips.append(create_clip(
        'temp/suspeito-de-invadir-clinica-veterinaria-e-preso-pela-bm'))

    clips.append(create_clip(
        'temp/tupinamba-vai-a-final-da-segundona-contra-o-sport'))

    video = concatenate_videoclips(clips)
    video.write_videofile('outputs/moviepy_complete.mp4')


if __name__ == '__main__':
    main()
