my_list = [57.8, 46.51, 97, 36.57, 44.60, 12.06, 34, 78.99, 654.55, 7.09, 99.99]
str_with_prices = ''
kopeiki = 0
for price in my_list:
    str_with_prices = ''.join([str_with_prices, str(int(price)), ' руб '])
    kopeiki = int((round(price - int(price), 2)) * 100)
    if kopeiki == 0:
        str_with_prices = ''.join([str_with_prices, ' 00 коп, '])
    elif kopeiki < 10:
        str_with_prices = ''.join([str_with_prices, '0', str(kopeiki), ' коп, '])
    else:
        str_with_prices = ''.join([str_with_prices, str(kopeiki), ' коп, '])
print(str_with_prices)

# Сортирую цены в том же списке
print(id(my_list))
my_list.sort()
print(my_list)
print(id(my_list))
# сортирую цены в новом списке
print(id(my_list))
my_list = sorted(my_list, reverse=True)
print(my_list)
print(id(my_list))

# вывожу 5 самых дорогих товаров
print(my_list[:5])
