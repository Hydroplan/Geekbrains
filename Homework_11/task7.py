class ComplexNumbers:
    def __init__(self, a, b):
        self.number = {'a': a, 'b*i': b}

    def __add__(self, other):
        result_a = self.number['a'] + other.number['a']
        result_bi = self.number['b*i'] + other.number['b*i']
        return ComplexNumbers(result_a, result_bi)

    def __mul__(self, other):
        result_a = self.number['a'] * other.number['a'] - \
                   self.number['b*i'] * other.number['b*i']

        result_bi = self.number['a'] * other.number['b*i'] + \
                    self.number['b*i'] * other.number['a']

        return ComplexNumbers(result_a, result_bi)


comlex_one = ComplexNumbers(2, 1)
comlex_two = ComplexNumbers(3, 4)

complex_tree = comlex_one + comlex_two
print(complex_tree.number)

complex_tree = comlex_one * comlex_two
print(complex_tree.number)
