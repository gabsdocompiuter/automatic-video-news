from news_reader import JornalDoPovo
from text_to_speech import Speech
from video_maker import VideoMaker

import image_manager


def run() -> None:
    jp = JornalDoPovo()
    vk = VideoMaker()

    headlines = jp.get_headlines(limit=10)
    for headline in headlines:
        print(headline)
        image_file = image_manager.download_image(
            headline.image_url,
            output_dir='temp',
            name=headline.id
        )

        sp = Speech()
        sp.add_phrase(headline.title)
        sp.add_phrase(headline.description)
        audio_file = sp.save(f'temp/{headline.id}')

        vk.create_clip(image_file, audio_file)
        print()

    vk.save_video(f'outputs/teste_10_news')


if __name__ == '__main__':
    run()
