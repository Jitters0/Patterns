from typing import List, Dict


class Shared:
    def __init__(self, company: str, position: str):
        self.__company = company
        self.__position = position

    @property
    def company(self):
        return self.__company

    @property
    def position(self):
        return self.__position


class Unique:
    def __init__(self, name: str, passport: str):
        self.__name = name
        self.__passport = passport

    @property
    def name(self):
        return self.__name

    @property
    def passport(self):
        return self.__passport


class Flyweight:
    def __init__(self, shared: Shared):
        self.__shared = shared

    def process(self, unique: Unique):
        print(f'Отображаем новые данные: общие - {self.__shared.company}_{self.__shared.position} и уникальные '
              f'{unique.name}_{unique.passport}')

    def get_data(self) -> str:
        return self.__shared.company + '_' + self.__shared.position


class FlyweightFactory:
    def __init__(self, shareds: List[Shared]):
        self.__flyweights: Dict[str, Flyweight] = {}
        for shared in shareds:
            self.__flyweights[self.get_key(shared)] = Flyweight(shared)

    def get_key(self, shared: Shared):
        return f'{shared.company}_{shared.position}'

    def get_flyweight(self, shared: Shared):
        key: str = self.get_key(shared)
        if self.__flyweights.get(key) is None:
            print(f'Фабрика легковесов: Общий объект по ключу {key} не найден. Создаем новый.')
            self.__flyweights[key] = Flyweight(shared)
        else:
            print(f'Фабрика легковесов: Извлекаем данные из имеющихся записей по ключу {key}.')
        return self.__flyweights[key]

    def list_flyweights(self):
        count: int = len(self.__flyweights)
        print(f'Фабрика легковесов: Всего {count} записей.')
        for pair in self.__flyweights.values():
            print(pair.get_data())


def add_specialist_database(ff: FlyweightFactory, company: str, position: str, name: str, passport: str):
    print()
    flyweight = ff.get_flyweight(Shared(company, position))
    flyweight.process(Unique(name, passport))


if __name__ == '__main__':
    shared_list: List[Shared] = [Shared('Blizzard', 'Гейм-дизайнер'),
                                 Shared('Apple', 'IOS-разработчик'),
                                 Shared('Samsung', 'Инженер'),
                                 Shared('Google', 'Android-разработчик')]

    factory = FlyweightFactory(shared_list)
    factory.list_flyweights()

    add_specialist_database(factory, 'Samsung', 'Инженер', 'Антон', '12312313')

    add_specialist_database(factory, 'Blizzard', 'Директор', 'Вася', '11133322')

    factory.list_flyweights()
