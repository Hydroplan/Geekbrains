my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list_updated = []

for element in my_list:
    if element.find('+') != -1:
        element = element.replace('+', '')
        if element.isdigit():
            if (int(element) / 10) < 1:
                my_list_updated.append('"')
                element = ''.join(['+0', element])
                my_list_updated.append(element)
                my_list_updated.append('"')

    elif element.isdigit():
        if (int(element) / 10) < 1:
            my_list_updated.append('"')
            element = ''.join(['0', element])
            my_list_updated.append(element)
            my_list_updated.append('"')

        else:
            my_list_updated.append('"')
            my_list_updated.append(element)
            my_list_updated.append('"')
    else:
        my_list_updated.append(element)
new_str = ''
for element in my_list_updated:
    new_str = ' '.join([new_str, element])

# Убираю лишний пробел в начале
new_str = new_str[1:]

print(my_list_updated)
print(new_str)
# Тут я заморочился с переключателями True, False, чтобы удалить лишние пробелы между кавычками и цифрами
format_new_string = ''
quotes_counter = 0
delete_next_gap = False
looking_for_second_gap = False

for symbol in new_str:
    if looking_for_second_gap:
        if symbol == ' ':
            looking_for_second_gap = False
            continue

    if delete_next_gap:
        delete_next_gap = False
        looking_for_second_gap = True
        continue
    if symbol == '"':
        quotes_counter += 1
        if quotes_counter % 2 != 0:
            delete_next_gap = True

    format_new_string = ''.join([format_new_string, symbol])

print(format_new_string)
