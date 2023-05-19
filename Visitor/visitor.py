from abc import ABC, abstractmethod
from typing import List


class AbstractVisitor(ABC):
    @abstractmethod
    def visit(self, place: 'AbstractPlace'):
        pass


class AbstractPlace(ABC):
    @abstractmethod
    def accept(self, visitor: AbstractVisitor):
        pass


class Zoo(AbstractPlace):
    def accept(self, visitor: AbstractVisitor):
        visitor.visit(self)


class Cinema(AbstractPlace):
    def accept(self, visitor: AbstractVisitor):
        visitor.visit(self)


class Cafe(AbstractPlace):
    def accept(self, visitor: AbstractVisitor):
        visitor.visit(self)


class Bob(AbstractVisitor):
    def __init__(self):
        self.value = ''

    def visit(self, place: AbstractPlace):
        if isinstance(place, Zoo):
            self.value = 'Слон в зоопарке'
        elif isinstance(place, Cinema):
            self.value = 'Фильм в кино'
        elif isinstance(place, Cafe):
            self.value = 'Кофе))0)'


if __name__ == '__main__':
    places: List[AbstractPlace] = [Zoo(), Cinema(), Cafe()]
    for place in places:
        visitor = Bob()
        place.accept(visitor)
        print(visitor.value)
