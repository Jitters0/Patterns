from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name: str):
        self._item_name: str = name
        self._owner_name: str = None

    def set_owner(self, o: str):
        self._owner_name = o

    @abstractmethod
    def add(self, sub_item: 'Item'):
        pass

    @abstractmethod
    def remove(self, sub_item: 'Item'):
        pass

    @abstractmethod
    def display(self):
        pass


class ClickableItem(Item):

    def __init__(self, name: str):
        super().__init__(name)

    def add(self, sub_item: Item):
        raise Exception('Кликабельному элементу нельзя добавить под-элемент')

    def remove(self, sub_item: Item):
        raise Exception('У кликабельного элемента не могут быть под-элементы')

    def display(self):
        print(self._owner_name + self._item_name)


class DropDownItem(Item):
    def __init__(self, name: str):
        super().__init__(name)
        self.__children = []

    def add(self, sub_item: Item):
        sub_item.set_owner(self._item_name)
        self.__children.append(sub_item)

    def remove(self, sub_item: Item):
        self.__children.remove(sub_item)

    def display(self):
        for item in self.__children:
            if self._owner_name is not None:
                print(self._owner_name, end='')
            item.display()


if __name__ == '__main__':
    file: Item = DropDownItem('файл->')

    create: Item = DropDownItem('Создать->')
    open_: Item = DropDownItem('Открыть->')
    exit_: Item = ClickableItem('Выход')

    file.add(create)
    file.add(open_)
    file.add(exit_)

    project: Item = ClickableItem('Проект...')
    repository: Item = ClickableItem('Репозиторий...')

    create.add(project)
    create.add(repository)

    solution: Item = ClickableItem('Решение...')
    folder = ClickableItem('Папка...')

    open_.add(solution)
    open_.add(folder)

    file.display()
    print()

    file.remove(create)

    file.display()



