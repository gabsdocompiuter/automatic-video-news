import pyttsx3

class Speech:
    def __init__(self: object) -> None:
        self.__phrases = ''
        self.__engine = pyttsx3.init()

    def add_phrase(self: object, phrase: str) -> None:
        self.__phrases += f'\r\n{phrase}'

    def save(self: object, filename='speech', extension='mp3') -> None:
        file = f'{filename}.{extension}'

        self.__engine.save_to_file(self.__phrases, file)
        self.__engine.runAndWait()