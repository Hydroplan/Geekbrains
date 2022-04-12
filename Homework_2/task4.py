my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for element in my_list:
    name = element.split()[-1]
    name = name.lower().capitalize()
    print('Привет, ' + name)

