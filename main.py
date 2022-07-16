from functions import invitation, handle_request, check_storage, courier_info
from myclass import Store, Shop


def main():
    invitation()
    count, item, destination_from, destination_to = handle_request()
    store = Store({'собачки': 5}, 100)
    shop = Shop({}, 20)
    if check_storage(count, item, store, shop):
        store.remove(item, count)
        print(courier_info('take'))
        print(courier_info('delivering'))
        shop.add(item, count)
        print(courier_info('delivered'))
    return f'Transportation can not be proceed.'


if __name__ == '__main__':
    main()
