from abc import ABC, abstractmethod
from typing import Dict


class AbstractSite(ABC):
    @abstractmethod
    def get_page(self, num: int) -> str:
        pass


class Site(AbstractSite):
    def get_page(self, num: int) -> str:
        return f'Это страница {num}'


class SiteProxy(AbstractSite):
    def __init__(self, site: AbstractSite):
        self.__site = site
        self.__cache: Dict[int, str] = {}

    def get_page(self, num: int) -> str:
        page: str = ''
        if self.__cache.get(num) is not None:
            page = self.__cache[num]
            page = 'Из кэша: ' + page
        else:
            page = self.__site.get_page(num)
            self.__cache[num] = page
        return page


if __name__ == '__main__':
    my_site: AbstractSite = SiteProxy(Site())

    print(my_site.get_page(1))
    print(my_site.get_page(2))
    print(my_site.get_page(3))

    print(my_site.get_page(2))
