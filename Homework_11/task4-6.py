class NotDigit(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse:
    capacity = 1000
    products = []

    def priemka(self):
        id_of_product = input('Введите код товара: ')
        amount = input('Введите количество товара: ')
        while not amount.isdigit():
            try:
                raise NotDigit('Ввели не число!!!')
            except NotDigit:
                print('Ввели не число!!!')
            amount = input('Введите количество товара: ')
        location = input('Введите название склада: ')
        new_stuff = {'id_of_product': id_of_product,
                     'amount': amount,
                     'location': location}
        if self.capacity < int(amount):
            print('Принимать некуда, нет места на складе')
        else:
            print('Успешная приемка')
            self.capacity -= int(amount)

            self.products.append(new_stuff)
        return new_stuff


class Orgtechnika:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


class Printer(Orgtechnika):
    def __init__(self, speed_of_printing, brand, price):
        super().__init__(brand, price)
        self.speed_of_printing = speed_of_printing


class Skaner(Orgtechnika):
    def __init__(self, speed_of_skanning, brand, price):
        super().__init__(brand, price)
        self.speed_of_skanning = speed_of_skanning


class Xerox(Orgtechnika):
    def __init__(self, speed_of_copying, brand, price):
        super().__init__(brand, price)
        self.speed_of_copying = speed_of_copying


hp_3310 = Skaner(5, 'HP', 4000)
epson_4g56 = Printer(10, 'Epson', 3000)
warehouse = Warehouse()
warehouse.priemka()
print(f'На складе осталось места: {warehouse.capacity}')
print(warehouse.products)