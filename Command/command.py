from abc import ABC, abstractmethod
from typing import List, Deque


class AbstractCommand(ABC):
    @abstractmethod
    def positive(self):
        pass

    @abstractmethod
    def negative(self):
        pass


class Engine:
    def start_engine(self):
        print('Двигатель запущен')

    def stop_engine(self):
        print('Двигатель остановлен')

    def increase_engine_speed(self):
        print('Обороты двигателя повышены')

    def decrease_engine_speed(self):
        print('Обороты двигателя снижены')


class EngineWorkCommand(AbstractCommand):
    def __init__(self, engine: Engine):
        self.engine: Engine = engine

    def positive(self):
        self.engine.start_engine()

    def negative(self):
        self.engine.stop_engine()


class EngineSpeedCommand(AbstractCommand):
    def __init__(self, engine: Engine):
        self.engine: Engine = engine

    def positive(self):
        self.engine.increase_engine_speed()

    def negative(self):
        self.engine.decrease_engine_speed()


class Controller:
    def __init__(self):
        self.__commands: List[AbstractCommand] = [None, None]
        self.__history: Deque[AbstractCommand] = []

    def set_command(self, button: int, command: AbstractCommand):
        self.__commands[button] = command

    def press_on(self, button: int):
        self.__commands[button].positive()
        self.__history.append(self.__commands[button])

    def press_cancel(self):
        if len(self.__history) != 0:
            self.__history.pop().negative()


if __name__ == '__main__':
    engine = Engine()

    controller = Controller()
    controller.set_command(0, EngineWorkCommand(engine))
    controller.set_command(1, EngineSpeedCommand(engine))

    controller.press_on(0)
    controller.press_on(1)
    controller.press_cancel()
    controller.press_cancel()

