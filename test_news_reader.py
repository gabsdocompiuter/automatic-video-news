from news_reader import JornalDoPovo, News

jp = JornalDoPovo()
for hl in jp.get_headlines():
    print(hl.title)
    print(hl.image_url)
    print()