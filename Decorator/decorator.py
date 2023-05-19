from abc import ABC, abstractmethod


class AbstractSender(ABC):

    @abstractmethod
    def send(self):
        pass


class Sender(AbstractSender):
    def __init__(self, data: str):
        self.__data = data

    def send(self):
        print(f'Отправляю данные: \"{self.__data}\"')


class Decorator(AbstractSender):
    def __init__(self, sender: AbstractSender):
        self._sender = sender

    @abstractmethod
    def send(self):
        self._sender.send()


class Compressor(Decorator):
    def __init__(self, sender: AbstractSender):
        super().__init__(sender)

    def send(self):
        print('Сжимаются данные > ', end='')
        self._sender.send()


class Encryptor(Decorator):
    def __init__(self, sender: AbstractSender):
        super().__init__(sender)

    def send(self):
        print('Шифрую данные > ', end='')
        self._sender.send()


if __name__ == '__main__':
    sender: AbstractSender = Sender('Hello World')
    sender.send()
    print()

    compressor: Decorator = Compressor(sender)
    compressor.send()
    print()

    encryptor: Decorator = Encryptor(compressor)
    encryptor.send()
