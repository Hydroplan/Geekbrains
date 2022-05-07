import sys
input_params = sys.argv
with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(f'{input_params[1]}\n')