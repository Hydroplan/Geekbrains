'''
 *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
должен быть с заглавной. Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
'''


def num_translate_adv(number: str):
    vocabulary = {'one': 'один', 'two': 'два', 'tree': 'три', 'four': 'четыре',
                  'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
                  'nine': 'девять', 'ten': 'десять'}

    if number[0].isupper():
        return vocabulary.get(number.lower()).capitalize()

    return vocabulary.get(number)


if __name__ == "__main__":
    print(num_translate_adv('One'))
    print(num_translate_adv('six'))
