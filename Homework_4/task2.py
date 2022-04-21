import requests


def currency_rates(char_code_inside):
    site_info = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    index_of_char_code = site_info.text.find(char_code_inside.upper())
    if index_of_char_code == -1: return None
    # print(site_info.text)
    index_of_value = site_info.text[index_of_char_code:].find('Value') + index_of_char_code

    result = site_info.text[(index_of_value + 6):(index_of_value + 13)]
    result_date = site_info.text[site_info.text.find('Date')+6:site_info.text.find('Date')+16]
    return float(result.replace(',', '.')), result_date

# Код для ручного ввода любой валюты
# char_code = input('Введите код валюты:')
# char_code_value = currency_rates(char_code)
#
# if char_code_value:
#     print('На ' + char_code_value[1] + ': ' + str(char_code_value[0]) + ' рублей за один ' + char_code.upper())
# else:
#     print('Ошибка при вводе валюты')

print(f'На {currency_rates("eur")[1]} курс евро: {currency_rates("EUR")[0]}, курс доллара: {currency_rates("USD")[0]}')
