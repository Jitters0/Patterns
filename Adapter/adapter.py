from abc import ABC, abstractmethod


class AbstractSystem(ABC):
    @abstractmethod
    def get_distance(self) -> float:
        pass


class MetricSystem(AbstractSystem):
    def __init__(self, current_distance: float):
        self.__current_distance = current_distance

    def get_distance(self) -> float:
        return self.__current_distance


class ImpericSystem(AbstractSystem):
    def __init__(self, current_distance: float):
        self.__current_distance = current_distance

    def get_distance(self) -> float:
        return self.__current_distance


class AdapterForImpericSystem(AbstractSystem):

    def __init__(self, imperic_system: ImpericSystem):
        self.__imperic_system = imperic_system

    def get_distance(self) -> float:
        return self.__imperic_system.get_distance() * 1.6


if __name__ == '__main__':
    km: float = 10.1
    miles: float = 10.1

    m_system = MetricSystem(km)
    miles_system = AdapterForImpericSystem(ImpericSystem(miles))

    print(m_system.get_distance())
    print(miles_system.get_distance())
