from constants import ACTIONS


def invitation():
    """Стартовое приглашение."""
    return f'Welcome!'


def handle_request():
    """
    Обработка запроса.
    Возвращает строку с запросом.
    """
    request = input('What kind of product do you want to transfer?')
    parsed_request = request.split()
    count = int(parsed_request[1])
    item = parsed_request[2]
    destination_from = parsed_request[4]
    destination_to = parsed_request[6]

    return count, item, destination_from, destination_to


def check_storage(
        count,
        item,
        store: 'Store',
        shop: 'Shop'
):
    """
    Проверяет, можно ли выполнить запрос пользователя.
    Запрашивает наличие товара в точке А и проверяет емкость точки Б.
    Возвращает True, если операция возможна.
    """
    if item not in store.items:
        return False
    if int(count) > int(store.items[item]):
        return False
    if not shop.get_free_space() >= int(count):
        return False

    return True


def courier_info(action):
    """Уведомляет о статусе перемещения товара."""
    return ACTIONS[action]
