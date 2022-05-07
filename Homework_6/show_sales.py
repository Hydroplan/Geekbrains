import sys
input_params = sys.argv
with open('bakery.csv', 'r', encoding='utf-8') as f:
    sales_data = f.read().split('\n')
    if len(input_params) == 1:
        print(sales_data)
    elif len(input_params) == 2:
        print(sales_data[int(input_params[1])-1:])
    elif len(input_params) == 3:
        print(sales_data[int(input_params[1]) - 1:int(input_params[2])])
