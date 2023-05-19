from abc import ABC, abstractmethod


class Phone:
    def __init__(self):
        self.data: str = ''

    @abstractmethod
    def about_phone(self) -> str:
        return self.data

    @abstractmethod
    def append_data(self, string: str):
        self.data += string


class AbstractDeveloper(ABC):
    @abstractmethod
    def create_display(self):
        pass

    @abstractmethod
    def create_box(self):
        pass

    @abstractmethod
    def system_install(self):
        pass

    @abstractmethod
    def get_phone(self) -> Phone:
        pass


class AndroidDeveloper(AbstractDeveloper):

    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data('Произведен дисплей Samsung;')

    def create_box(self):
        self.__phone.append_data('Произведен корпус Samsung;')

    def system_install(self):
        self.__phone.append_data('Установлена система Android;')

    def get_phone(self) -> Phone:
        return self.__phone


class AppleDeveloper(AbstractDeveloper):

    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data('Произведен дисплей Apple;')

    def create_box(self):
        self.__phone.append_data('Произведен корпус Apple;')

    def system_install(self):
        self.__phone.append_data('Установлена система IOS;')

    def get_phone(self) -> Phone:
        return self.__phone


class Director:
    def __init__(self, developer: AbstractDeveloper):
        self.__developer = developer

    def set_developer(self, developer: AbstractDeveloper):
        self.__developer = developer

    def mount_only_phone(self) -> Phone:
        self.__developer.create_box()
        self.__developer.create_display()
        return self.__developer.get_phone()

    def mount_full_phone(self) -> Phone:
        self.__developer.create_box()
        self.__developer.create_display()
        self.__developer.system_install()
        return self.__developer.get_phone()


if __name__ == '__main__':
    android_developer: AbstractDeveloper = AndroidDeveloper()

    director = Director(android_developer)

    samsung: Phone = director.mount_full_phone()
    print(samsung.about_phone())

    iphone_developer: AbstractDeveloper = AppleDeveloper()

    director.set_developer(iphone_developer)
    iphone: Phone = director.mount_only_phone()
    print(iphone.about_phone())
