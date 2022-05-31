class Cell:
    def __init__(self, num_of_elements):
        self.num_of_elements = num_of_elements

    def __add__(self, other):
        return self.num_of_elements + other.num_of_elements

    def __sub__(self, other):

        if self.num_of_elements - other.num_of_elements == 0:
            print('Клетки самоуничтожились')
            raise ValueError
        result = self.num_of_elements - other.num_of_elements
        if result < 0:
            result = result * (-1)

        return result

    def __mul__(self, other):
        return self.num_of_elements * other.num_of_elements

    def __truediv__(self, other):
        return max(self.num_of_elements, other.num_of_elements) // \
               min(self.num_of_elements, other.num_of_elements)

    def make_order(self, elem_in_row):
        result = ''
        for i in range(self.num_of_elements // elem_in_row):
            result = ''.join([result, "*" * elem_in_row,'\n'])
        if self.num_of_elements % elem_in_row:
            result = ''.join([result, "*" * (self.num_of_elements % elem_in_row), '\n'])
        return result


cell_one = Cell(10)
cell_two = Cell(21)
print(cell_one + cell_two)
print(cell_one - cell_two)
print(cell_one * cell_two)
print(cell_one / cell_two)
print(cell_two.make_order(5))
