class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        result = ''
        for el in self.list_of_lists:
            result = ''.join([result, f'{el}\n'])
        return result

    def __add__(self, other):
        result_row = []
        result_matrix = []
        for i in range(0, len(self.list_of_lists)):

            for j in range(0, len(self.list_of_lists[i])):

                result_row.append(self.list_of_lists[i][j] + other.list_of_lists[i][j])

            result_matrix.append(result_row)
            result_row = []

        return result_matrix


matr_one = Matrix([[1, 2, 6], [3, 4, 5]])
matr_two = Matrix([[1, 2, 6], [3, 4, 5]])
print(matr_one)
matr_tree = Matrix(matr_one + matr_two)
print(matr_tree)