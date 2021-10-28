class News:
    def __init__(self: object, title='', image_url='', link='', datetime=None) -> None:
        self.title = title
        self.image_url = image_url
        self.link = link
        self.datetime = datetime

    def __str__(self) -> str:
        return self.title