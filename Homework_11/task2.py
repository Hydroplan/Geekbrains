class ZeroDivision(Exception):
    def __init__(self, message):
        self.message = message




a = 100
b = input('Введите делитель b ')
b = int(b)
try:
    if b == 0:
        raise ZeroDivision('Делишь на ноль!!!')
except ZeroDivision as err:
    print(err)
except Exception:
    print('Какая-то ошибка')
else:
    c = a/int(b)
    print(c)
