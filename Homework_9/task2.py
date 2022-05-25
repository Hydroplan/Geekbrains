class Road:

    def __init__(self, lenght, widht):
        self.__lenght = lenght
        self.__widht = widht

    def masscount(self, mass_of_1_sm, height):
        return f'{self.__lenght * self.__widht * mass_of_1_sm * height} кг'


doroga = Road(10000, 10)
print(doroga.masscount(25, 5))
