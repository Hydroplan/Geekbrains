src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

work_list = []
list_of_doubles = []
for el in src:
    if el in work_list:
        list_of_doubles.append(el)
        continue
    else:
        work_list.append(el)
for el in list(set(list_of_doubles)):
    work_list.remove(el)

print(work_list)
