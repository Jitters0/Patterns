from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def release(self):
        pass


class Latte(Product):
    def release(self):
        print('Сделано латте')


class Espresso(Product):
    def release(self):
        print('Сделано эспрессо')


class CoffeMachine(ABC):
    @abstractmethod
    def make_coffe(self):
        pass


class LatteMachine(CoffeMachine):
    def make_coffe(self):
        print('Готовиться латте')
        return Latte()


class EspressoMachine(CoffeMachine):
    def make_coffe(self):
        print('Готовиться эспрессо')
        return Espresso()


if __name__ == '__main__':
    machine = LatteMachine()
    latte = machine.make_coffe()
    latte.release()

    machine = EspressoMachine()
    espresso = machine.make_coffe()
    espresso.release()
