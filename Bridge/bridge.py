from abc import ABC, abstractmethod


class AbstractDataReader(ABC):
    @abstractmethod
    def read(self):
        pass


class DatabaseReader(AbstractDataReader):
    def read(self):
        print('Данные из базы данных ', end='')


class FileReader(AbstractDataReader):
    def read(self):
        print('Данные из файла ', end='')


class Sender(ABC):

    def __init__(self, data_reader: AbstractDataReader):
        self.reader: AbstractDataReader = data_reader

    def set_data_reader(self, data_reader: AbstractDataReader):
        self.reader: AbstractDataReader = data_reader

    @abstractmethod
    def send(self):
        pass


class EmailSender(Sender):
    def __init__(self, data_reader: AbstractDataReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print('отправленные при помощи Email')


class TelegramBotSender(Sender):
    def __init__(self, data_reader: AbstractDataReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print('отправленные при помощи Telegram')


if __name__ == '__main__':
    sender: Sender = EmailSender(DatabaseReader())
    sender.send()

    sender.set_data_reader(FileReader())
    sender.send()

    sender = TelegramBotSender(DatabaseReader())
    sender.send()
