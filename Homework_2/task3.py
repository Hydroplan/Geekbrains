my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_str = ''
for element in my_list:
    if element.find('+') != -1:
        element = element.replace('+', '')
        if element.isdigit():
            if (int(element) / 10) < 1:
                element = ''.join(['"+0', element])
                element = ''.join([element, '"'])

    if element.isdigit():
        if (int(element) / 10) < 1:
            element = ''.join(['"0', element])
            element = ''.join([element, '"'])
        else:
            element = ''.join(['"', element])
            element = ''.join([element, '"'])
    new_str = ' '.join([new_str, element])

print(new_str)

