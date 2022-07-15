from functions import invitation, handle_request, check_storage, courier_info
from myclass import Store, Shop
# from constants import ACTIONS


def main():
    invitation()
    count, item, destination_from, destination_to = handle_request()
    store = Store({'собачки': 5}, 100)
    shop = Shop({}, 20)
    if check_storage(count, item, store, shop):
        store.remove(item, count)
        print(f'на складе осталось {store.items}')
        shop.add(item, count)
        print(f'в магазине сейчас {shop.items}')
    return f'Transportation can not be proceed.'


if __name__ == '__main__':
    main()
