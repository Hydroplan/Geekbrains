class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}

    def get_total_income(self):  # скрытые атрибуты могу вызвать только из родительского класса
        return f"Общий доход {self.__income['wage'] + self.__income['bonus']} руб"


class Position(Worker):
    def get_full_name(self):
        return f'{self.position} {self.name} {self.surname}'


frezerovshik = Position('Ivan', 'Petrovich', 'Frezerovshik', 50000, 15000)
print(frezerovshik.get_full_name())
print(frezerovshik.get_total_income())
