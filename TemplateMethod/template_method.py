from abc import ABC, abstractmethod


class Transmitter(ABC):
    def get_message(self):
        print('Получаю сообщение')

    def encryption(self):
        pass

    def vpn(self):
        pass

    def send_message(self):
        print('Передаю сообщение')

    def start(self):
        self.get_message()
        self.encryption()
        self.vpn()
        self.send_message()


class Telegram(Transmitter):
    def encryption(self):
        print('Шифрую сообщение')


class Email(Transmitter):
    def encryption(self):
        print('Шифрую сообщение')

    def vpn(self):
        print('Включаю впн')


if __name__ == '__main__':
    telegram = Telegram()
    email = Email()

    telegram.start()
    print('------------------')
    email.start()
