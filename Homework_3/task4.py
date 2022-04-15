"""
*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
записи, в которых фамилия начинается с соответствующей буквы. Например:
>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр
Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
        },
    "И": {
        "И": ["Илья Иванов"]
        },
    "С": {
            "И": ["Иван Сергеев", "Инна Серова"],
            "А": ["Анна Савельева"]
        }
}
Как поступить, если потребуется сортировка по ключам?
"""


def thesaurus(*args):
    result_dict = {}
    for arg in args:
        splitted_arg = arg.split()
        name_first_letter = splitted_arg[0][0]
        surname_first_letter = splitted_arg[1][0]
        if result_dict.get(surname_first_letter) is None:
            result_dict[surname_first_letter] = {}
        if result_dict[surname_first_letter].get(name_first_letter) is None:
            result_dict[surname_first_letter][name_first_letter] = []
            print(result_dict)
        result_dict[surname_first_letter][name_first_letter].append(arg)

    return result_dict


if __name__ == "__main__":
    print(thesaurus("Иван Сергеев", "Инна Серова",
                    "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
