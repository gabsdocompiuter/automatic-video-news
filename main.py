from automatic_video_news import AutomaticVideoNews


def main() -> None:
    video_news = AutomaticVideoNews()

    video_news.read_news(jornal_povo=True)

    video_news.create_video('jp')


if __name__ == '__main__':
    main()
