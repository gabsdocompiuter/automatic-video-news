from news_reader import JornalDoPovo
from text_to_speech import Speech

import image_manager

def run() -> None:
    jp = JornalDoPovo()
    headlines = jp.get_headlines(limit=3)
    for headline in headlines:
        print(headline)
        image = image_manager.download_image(headline.image_url)
        print(image)

if __name__ == '__main__':
    run()
