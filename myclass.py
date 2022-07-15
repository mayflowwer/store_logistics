from abc import ABC


class Storage(ABC):
    """Абстрактный класс хранилица."""
    items: dict = {}
    capacity: int = 0

    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def get_items(self):
        """Возвращает кол-во айтемов и их кол-ва в storage."""
        return self.items

    def get_free_space(self):
        """Возвращает кол-во свободного места в storage."""
        stored = 0
        for count in self.items.values():
            stored += count
        return int(self.capacity - stored)

    def get_unique_items_count(self):
        """Возвращает кол-во уникальных товаров."""
        items = {item: count for (item, count) in self.items.items()}
        return items

    def add(self, item, count):
        """Добавляет items к items в классе."""
        if item in self.items:
            self._items[item] += count
        else:
            self._items[item] = count

    def remove(self, item, count):
        """Забирает кол-во айтемов от кол-ву айтемов класса."""
        if item in self.items:
            self._items[item] -= count
        else:
            raise Exception('Storage does not have such item.')


class Store(Storage):
    """Класс Склад."""
    def __init__(self, items, capacity):
        super().__init__(items, capacity=100)
        self._items = items
        self._capacity = capacity

    def __repr__(self):
        return f'store'

    def add(self, item, count):
        """Добавляет item в storage при наличии свободного места."""
        free_space = self.get_free_space()
        if free_space >= free_space + count:
            if item in self.items:
                self._items[item] += count
            else:
                self._items[item] = count
        else:
            raise Exception('Storage does not have more free space.')

    def remove(self, item, count):
        """Уменьшает кол-во items, но не меньше 0."""
        current_item_count = self.items.get(item)
        if not current_item_count:
            raise Exception('There is no such item in store.')
        if current_item_count >= count:
            self._items[item] -= count


class Shop(Storage):
    """Класс Магазин."""
    def __init__(self, items, capacity):
        super().__init__(items, capacity=20)
        self._items = items
        self._capacity = capacity

    def __repr__(self):
        return f'shop'

    def add(self, item, count):
        """Добавляет item в storage при наличии свободного места."""
        free_space = self.get_free_space()
        if not free_space >= count:
            raise Exception('There is no free space in the shop.')
        if item not in self.items.keys():
            if not len(self.get_unique_items_count()) + 1 <= 5:
                raise Exception('The shop can contain only 5 unique items.')

            self._items[item] = count

        self._items[item] += count


class Request:
    """Класс Запрос."""
    _from: str
    _to: str
    _amount: int
    _product: str

    def __init__(self, storage_list: list, request: str):
        self.parsed_request = request.split()
        self._from = self.parsed_request[4]
        self._to = self.parsed_request[6]
        self._amount = int(self.parsed_request[1])
        self._product = self.parsed_request[2]
