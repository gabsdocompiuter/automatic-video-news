class News:
    def __init__(self: object, title='', description='', image_url='', link='', datetime=None) -> None:
        self.title = title
        self.description = description
        self.image_url = image_url
        self.link = link
        self.datetime = datetime

    def __str__(self) -> str:
        return f'{self.title}\r\n{self.description}'