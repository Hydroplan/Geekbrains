class NotDigit(Exception):
    def __init__(self, txt):
        self.txt = txt


input_data = ''
list_of_int = []
while not input_data == 'stop':
    input_data = input('Введите число в список, для остановки "stop": ')
    if input_data == 'stop':
        break
    if input_data.isdigit():

        list_of_int.append(input_data)
    else:
        try:
            raise NotDigit('Ввели не число!!!')
        except NotDigit:
            print('Ввели не число!!!')

print(list_of_int)
