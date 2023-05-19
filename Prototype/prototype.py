from abc import ABC
import copy

class Car:
    __model: str = ''
    __params: dict = {'Мотор': 'V8', 'Вес': 1420, 'Разгон': 4.3}

    def __init__(self, donor: 'Car' = None):
        if donor is not None:
            self.__model = donor.get_model()
            self.__params = copy.deepcopy(donor.get_params())



    def set_model(self, model: str):
        self.__model = model

    def get_model(self) -> str:
        return self.__model

    def get_params(self) -> dict:
        return self.__params

    def set_weight(self, new_weight: int):
        self.__params['Вес'] = new_weight

    def set_engine(self, new_motor: int):
        self.__params['Мотор'] = new_motor

    def set_speed(self, new_speed: int):
        self.__params['Разгон'] = new_speed

    def clone(self):
        return Car(self)


if __name__ == '__main__':
    car_donor: Car = Car()
    car_donor.set_model('BMW M5')

    car_clone: Car = car_donor.clone()

    print('Донор:', car_donor.get_model(), car_donor.get_params())
    print('Клон:', car_clone.get_model(), car_clone.get_params())

    car_clone.set_model('Tesla Model S')
    car_clone.set_weight(1680)
    car_clone.set_engine('Electric')
    car_clone.set_speed(2.8)

    print()
    print('Донор:', car_donor.get_model(), car_donor.get_params())
    print('Клон:', car_clone.get_model(), car_clone.get_params())