from abc import ABC, abstractmethod


class ProviderCommunication:
    def receive(self):
        print('Получении продукции от производителя')

    def payment(self):
        print('Оплата поставщику')


class Site:
    def placement(self):
        print('Размещение на сайте')

    def delete(self):
        print('Удаление с сайта')


class Database:
    def insert(self):
        print('Запись в базу данных')

    def delete(self):
        print('Удаление из базы данных')


class MarketPlace:
    def __init__(self):
        self._provider_communication = ProviderCommunication()
        self._site = Site()
        self._database = Database()

    def product_receipt(self):
        self._provider_communication.receive()
        self._site.placement()
        self._database.insert()

    def product_release(self):
        self._provider_communication.payment()
        self._site.delete()
        self._database.delete()


if __name__ == '__main__':
    market_place = MarketPlace()
    market_place.product_receipt()
    print()
    market_place.product_release()
