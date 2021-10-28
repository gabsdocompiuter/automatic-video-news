from news_reader import JornalDoPovo, News

jp = JornalDoPovo()
for hl in jp.get_headlines():
    print(hl)
    print(hl.image_url)
    print()