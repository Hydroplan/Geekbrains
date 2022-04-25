tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Никита', 'Андрей'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def gen_for_tutors(list_of_names, list_of_classes):
    for element in list_of_names:
        i = list_of_names.index(element)
        if i+1 > len(list_of_classes):
            result = [list_of_names[i], None]
            yield tuple(result)
        else:
            result = [list_of_names[i], list_of_classes[i]]
            yield tuple(result)


cortege_result = gen_for_tutors(tutors, classes)

print(next(cortege_result))
print(next(cortege_result))
print(next(cortege_result))
print(next(cortege_result))
print(next(cortege_result))
print(next(cortege_result))
print(next(cortege_result))
print(next(cortege_result))
print(next(cortege_result))
print(next(cortege_result))
