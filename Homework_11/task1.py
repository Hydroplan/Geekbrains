class Data:

    def __init__(self, dd_mm_yy):
        self.date = dd_mm_yy

    @classmethod
    def date_to_int(cls, date):

        date_int = [int(date[0:2]), int(date[3:5]), int(date[6:])]
        return date_int

    @staticmethod
    def date_validator(date):
        if int(date[0:2]) not in range(1,31):
            print("столько дней в месяце нет")
            raise ValueError
        if int(date[3:5]) not in range(1,12):
            print("столько месяцев в году нет")
            raise ValueError
        if int(date[6:]) not in range(1,99):
            print("год указан неверно")
            raise ValueError
        print("Дата в порядке")



new_data = Data('06-06-96')
print(Data.date_to_int(new_data.date))
new_data = Data('06-36-96')
Data.date_validator(new_data.date)