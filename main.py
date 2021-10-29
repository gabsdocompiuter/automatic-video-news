from news_reader import JornalDoPovo
from text_to_speech import Speech
from video_maker import VideoMaker

import image_manager

def run() -> None:
    jp = JornalDoPovo()
    headlines = jp.get_headlines(limit=3)
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

        vk = VideoMaker()
        vk.set_background(image_file)
        vk.set_audio(audio_file)
        vk.save_video(f'outputs/{headline.id}')
        print()

if __name__ == '__main__':
    run()
