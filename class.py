from abc import ABC, abstractmethod


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

    def add(self, item, count):
        """Добавляет кол-во айтемов к кол-ву айтемов класса."""
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

    def get_free_space(self):
        """Возвращает кол-во свободного места в storage."""
        free_space = 0
        for count in self.items.values():
            free_space += count
        return free_space

    def get_items(self):
        """Возвращает кол-во айтемов и их кол-ва в storage."""
        return self.items

    def get_unique_items_count(self):
        """Возвращает кол-во уникальных товаров."""
        items = [item for item in self.items.keys()]
        return items


class Store(Storage):
    """Класс Склад."""
    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)
        self._items = items
        self._capacity = capacity

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
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)
        self._items = items
        self._capacity = capacity

    def add(self, item, count):
        """Добавляет item в storage при наличии свободного места."""
        free_space = self.get_free_space()
        if not free_space >= free_space + count:
            raise Exception('There is no free space in the shop.')
        if item not in self.items.keys(): # доделать проверку уникальности item
            if len(self.get_unique_items_count()) + 1 <= 5:
                if item in self.items:
                    self._items[item] += count
                else:
                    self._items[item] = count
            else:
                raise Exception('Shop can contain only 5 unique items.')


shop = Shop({'apples': 2, 'bananas': 3, 'pineapples': 2, 'plums': 5, 'tea': 4})
print(shop.items)
shop.add('apples', 1)


