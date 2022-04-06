"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""


def naive_realisation(duration: int):
    total_time = ''
    """
    Решение задачи БЕЗ использования циклов.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """

    # YOUR CODE HERE
    # Сначала сделал такой код, первое что пришло в голову. Потом понял, что тут много лишнего и
    # получился вариант покороче :)

    # if duration >= 86400:
    #     days_amount = duration // 86400
    #     rest_of_seconds = duration % 86400
    #
    #     if rest_of_seconds >= 3600:
    #         hours_amount = rest_of_seconds // 3600
    #         rest_of_seconds = rest_of_seconds % 3600
    #         if rest_of_seconds >= 60:
    #             minutes_amount = rest_of_seconds // 60
    #             rest_of_seconds = rest_of_seconds % 60
    #             total_time = str(days_amount) + ' дн ' + str(hours_amount) + \
    #                          ' час ' + str(minutes_amount) + ' мин ' + str(rest_of_seconds) + ' сек '
    #         else:
    #             minutes_amount = 0
    #             total_time = str(days_amount) + ' дн ' + str(hours_amount) + \
    #                          ' час ' + str(minutes_amount) + ' мин ' + str(rest_of_seconds) + ' сек '
    #     else:
    #         hours_amount = 0
    #         if rest_of_seconds >= 60:
    #             minutes_amount = rest_of_seconds // 60
    #             rest_of_seconds = rest_of_seconds % 60
    #             total_time = str(days_amount) + ' дн ' + str(hours_amount) + \
    #                          ' час ' + str(minutes_amount) + ' мин ' + str(rest_of_seconds) + ' сек '
    #         else:
    #             minutes_amount = 0
    #             total_time = str(days_amount) + ' дн ' + str(hours_amount) + \
    #                          ' час ' + str(minutes_amount) + ' мин ' + str(rest_of_seconds) + ' сек '
    # else:
    #     days_amount = 0
    #     rest_of_seconds = duration
    #
    #     if rest_of_seconds >= 3600:
    #         hours_amount = rest_of_seconds // 3600
    #         rest_of_seconds = rest_of_seconds % 3600
    #         if rest_of_seconds >= 60:
    #             minutes_amount = rest_of_seconds // 60
    #             rest_of_seconds = rest_of_seconds % 60
    #             total_time = str(days_amount) + ' дн ' + str(hours_amount) + \
    #                          ' час ' + str(minutes_amount) + ' мин ' + str(rest_of_seconds) + ' сек '
    #         else:
    #             minutes_amount = 0
    #             total_time = str(days_amount) + ' дн ' + str(hours_amount) + \
    #                          ' час ' + str(minutes_amount) + ' мин ' + str(rest_of_seconds) + ' сек '
    #     else:
    #         hours_amount = 0
    #         if rest_of_seconds >= 60:
    #             minutes_amount = rest_of_seconds // 60
    #             rest_of_seconds = rest_of_seconds % 60
    #             total_time = str(days_amount) + ' дн ' + str(hours_amount) + \
    #                          ' час ' + str(minutes_amount) + ' мин ' + str(rest_of_seconds) + ' сек '
    #         else:
    #             minutes_amount = 0
    #             total_time = str(days_amount) + ' дн ' + str(hours_amount) + \
    #                          ' час ' + str(minutes_amount) + ' мин ' + str(rest_of_seconds) + ' сек '
    #
    # return total_time
    if duration >= 86400:
        days_amount = duration // 86400
    else: days_amount = 0

    rest_of_seconds = duration % 86400

    if rest_of_seconds >= 3600:
        hours_amount = rest_of_seconds//3600

    else: hours_amount = 0

    rest_of_seconds = rest_of_seconds % 3600

    if rest_of_seconds >= 60:
        minutes_amount = rest_of_seconds // 60
    else: minutes_amount = 0

    rest_of_seconds = rest_of_seconds % 60

    total_time = str(days_amount) +' дн ' + str(hours_amount) + \
                             ' час ' + str(minutes_amount) + ' мин ' + str(rest_of_seconds) + ' сек '
    return total_time

def one_cycle_realisation(duration):
    total_time = ''
    """
    Решение задачи с использования циклов.
    Можно два, но высший пилотаж через 1 цикл.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужном формате
    """

    # YOUR CODE HERE
    seconds = 0
    minutes = 0
    hours = 0
    days = 0
    for i in range(1, duration + 1):
        seconds += 1
        if seconds > 59:
            minutes += 1
            seconds -= 60
            if minutes > 59:
                hours += 1
                minutes -= 60
                if hours > 23:
                    days += 1
                    hours -= 24

    total_time = str(days) + ' дн ' + str(hours) + \
                 ' час ' + str(minutes) + ' мин ' + str(seconds) + ' сек '
    return total_time


if __name__ == '__main__':
    duration = 628
    print(naive_realisation(duration))
    print(one_cycle_realisation(duration))