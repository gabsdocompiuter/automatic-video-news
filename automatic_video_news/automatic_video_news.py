from news_reader import News, JornalDoPovo
from text_to_speech import Speech
from video_maker import VideoMaker
from typing import List
import image_manager


class AutomaticVideoNews:
    def __init__(self: object) -> None:
        self.__headlines: List[News] = []

    def read_news(self: object, news_site_limit=10, jornal_povo=False) -> None:
        if jornal_povo:
            jp = JornalDoPovo()
            self.__headlines.extend(jp.get_headlines(limit=news_site_limit))

    def create_video(self: object, name: str) -> str:
        vk = VideoMaker()

        for headline in self.__headlines:
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

        video = vk.save_video(f'outputs/{name}')
        print(video)
