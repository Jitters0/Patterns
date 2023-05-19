from abc import ABC, abstractmethod


class AbstractEngine(ABC):
    @abstractmethod
    def release_engine(self):
        pass


class BmwEngine(AbstractEngine):
    def release_engine(self):
        print('Двигатель от BMW')


class MercedesEngine(AbstractEngine):
    def release_engine(self):
        print('Двигатель от Mercedes')


class AbstractCar(ABC):
    @abstractmethod
    def release_car(self, engine: AbstractEngine):
        pass


class BmwCar(AbstractCar):
    def release_car(self, engine: AbstractEngine):
        print('Собрали автомобиль BMW, ', end='')
        engine.release_engine()


class MercedesCar(AbstractCar):
    def release_car(self, engine: AbstractEngine):
        print('Собрали автомобиль Mercedes, ', end='')
        engine.release_engine()


class AbstractFactory(ABC):
    @abstractmethod
    def create_engine(self) -> AbstractEngine:
        pass

    @abstractmethod
    def create_car(self) -> AbstractCar:
        pass


class BmwFactory(AbstractFactory):
    def create_engine(self) -> AbstractEngine:
        return BmwEngine()

    def create_car(self) -> AbstractCar:
        return BmwCar()


class MercedesFactory(AbstractFactory):
    def create_engine(self) -> AbstractEngine:
        return MercedesEngine()

    def create_car(self) -> AbstractCar:
        return MercedesCar()


if __name__ == '__main__':
    bmw_factory = BmwFactory()
    bmw_engine = bmw_factory.create_engine()
    bmw_car = bmw_factory.create_car()

    mercedes_factory = MercedesFactory()
    mercedes_engine = mercedes_factory.create_engine()
    mercedes_car = mercedes_factory.create_car()

    bmw_car.release_car(bmw_engine)
    mercedes_car.release_car(mercedes_engine)
    mercedes_car.release_car(bmw_engine)


