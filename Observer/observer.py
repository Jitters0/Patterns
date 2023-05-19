from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self, p: int):
        pass


class Observable(ABC):
    @abstractmethod
    def add_observer(self, o: Observer):
        pass

    @abstractmethod
    def remove_observer(self, o: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Product(Observable):
    def __init__(self, price: int):
        self.__price = price
        self.__observers: List[Observer] = []

    def change_price(self, price: int):
        self.__price = price
        self.notify()

    def add_observer(self, o: Observer):
        self.__observers.append(o)

    def remove_observer(self, o: Observer):
        self.__observers.remove(o)

    def notify(self):
        for o in self.__observers:
            o.update(self.__price)


class Wholesale(Observer):
    def __init__(self, obj: Observable):
        self.__product = obj
        obj.add_observer(self)

    def update(self, p: int):
        if p < 300:
            print(f'Оптовик закупил товар по цене {p}')
            self.__product.remove_observer(self)


class Buyer(Observer):
    def __init__(self, obj: Observable):
        self.__product = obj
        obj.add_observer(self)

    def update(self, p: int):
        if p < 350:
            print(f'Покупатель закупил товар по цене {p}')
            self.__product.remove_observer(self)


if __name__ == '__main__':
    product = Product(400)
    wholesale = Wholesale(product)
    buyer = Buyer(product)

    product.change_price(320)
    product.change_price(280)
