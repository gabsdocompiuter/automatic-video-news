class News:
    def __init__(self: object, id='', title='', description='', image_url='', link='', datetime=None) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.image_url = image_url
        self.link = link
        self.datetime = datetime

    def __str__(self) -> str:
        return f'{self.id}\r\n{self.title}\r\n{self.description}'