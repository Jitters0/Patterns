from abc import ABC, abstractmethod
from typing import Deque


class Memento(ABC):
    @abstractmethod
    def get_dollars(self) -> int:
        pass

    @abstractmethod
    def get_euro(self) -> int:
        pass


class ExchangeMemento(Memento):
    def __init__(self, d: int, e: int):
        self.__dollars = d
        self.__euro = e

    def get_dollars(self) -> int:
        return self.__dollars

    def get_euro(self) -> int:
        return self.__euro


class Exchange:
    def __init__(self, d: int, e: int):
        self.__dollars = d
        self.__euro = e

    def get_dollars(self):
        print(f'Долларов: {self.__dollars}')

    def get_euro(self):
        print(f'Евро: {self.__euro}')

    def sell(self):
        if self.__dollars > 0:
            self.__dollars -= 1

    def buy(self):
        self.__euro += 1

    def save(self) -> ExchangeMemento:
        return ExchangeMemento(self.__dollars, self.__euro)

    def restore(self, exchange_memento: Memento):
        self.__dollars = exchange_memento.get_dollars()
        self.__euro = exchange_memento.get_euro()


class Memory:
    def __init__(self, exchange: Exchange):
        self.__exchange = exchange
        self.__history: Deque[Memento] = []

    def backup(self):
        self.__history.append(self.__exchange.save())

    def undo(self):
        if len(self.__history) == 0:
            return
        else:
            self.__exchange.restore(self.__history.pop())


if __name__ == '__main__':
    exchange = Exchange(d=10, e=10)

    memory = Memory(exchange)

    exchange.get_dollars()
    exchange.get_euro()

    print('Покупка доллара, продажа евро')
    exchange.sell()
    exchange.buy()

    exchange.get_dollars()
    exchange.get_euro()

    print('Сохранение состояния')
    memory.backup()

    print('Покупка доллара, продажа евро')
    exchange.sell()
    exchange.buy()

    exchange.get_dollars()
    exchange.get_euro()

    print('Восстановление состояния')
    memory.undo()

    exchange.get_dollars()
    exchange.get_euro()
