import requests


def currency_rates(char_code_inside):
    site_info = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    index_of_char_code = site_info.text.find(char_code_inside.upper())
    if index_of_char_code == -1: return None
    # print(site_info.text)
    index_of_value = site_info.text[index_of_char_code:].find('Value') + index_of_char_code

    result = site_info.text[(index_of_value + 6):(index_of_value + 13)]
    result_date = site_info.text[site_info.text.find('Date') + 6:site_info.text.find('Date') + 16]
    return float(result.replace(',', '.')), result_date
