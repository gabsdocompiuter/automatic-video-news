import requests

from .news import News
from bs4 import BeautifulSoup
from typing import List

class JornalDoPovo:
    def __init__(self: object) -> None:
        self.__endpoint = 'https://www.jornaldopovo.net/ultimas-noticias'

    def get_headlines(self: object) -> List[News]:
        headlines_scrapeds = self.__scrape_headlines()

        headlines = []
        for hl in headlines_scrapeds:
            headlines.append(self.__sanitize_headline(hl))

        return headlines

    def __scrape_headlines(self: object) -> BeautifulSoup:
        response = requests.get(self.__endpoint)
        content = response.content

        full_site = BeautifulSoup(content, 'html.parser')
        site_news = full_site.find('section', 'main-listing').find_all('div', 'grid--item')

        return site_news

    def __sanitize_headline(self: object, soup: BeautifulSoup) -> List[News]:
        title = soup.find('h4').find('a').text
        image_url = soup.find('img', src=True)['src']
        link = soup.find('h4').find('a', href=True)['href']
        description = soup.find('p').text

        return News(
            title=title,
            description=description,
            image_url=image_url,
            link=link
        )
