from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def parse(self, url: str):
        pass


class ResourceReader:
    def __init__(self, reader: Reader):
        self.__reader = reader

    def set_strategy(self, reader: Reader):
        self.__reader = reader

    def read(self, url: str):
        self.__reader.parse(url)


class NewsSiteReader(Reader):
    def parse(self, url: str):
        print('Парсинг новостного сайта:', url)


class SocialNetworkReader(Reader):
    def parse(self, url: str):
        print('Парсинг ленты новостей соц. сети:', url)


class TelegramChannelReader(Reader):
    def parse(self, url: str):
        print('Парсинг канала в Telegram:', url)


if __name__ == '__main__':
    resource_reader = ResourceReader(NewsSiteReader())

    url = 'https://news.com/'
    resource_reader.read(url)

    url = 'https://vk.com/'
    resource_reader.set_strategy(SocialNetworkReader())
    resource_reader.read(url)

    url = '@news'
    resource_reader.set_strategy(TelegramChannelReader())
    resource_reader.read(url)
