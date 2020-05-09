# 1
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

        def __str__(self):
            return '\n'.join(map(lambda r: '  '.join(map(str, r)), self.matrix)) + '\n'

        def __add__(self, other):
            return Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))


my_m1 = [[3, 5, 32], [3, 5, 8], [-3, -6, 2]]
my_m2 = [[3, 5, 32], [3, 5, 8], [-3, -6, 2]]
print(my_m1)
print(my_m2)
s = my_m1 + my_m2
print(s)

# 2
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

        @abstractmethod
        def consumption(self):
            pass


class Coat(Clothes):
    @property
    def consumption(self):
        return f"Consumption - {round(self.param / 6.5) + 0.5}"


class Costume(Clothes):
    @property
    def consumption(self):
        return f"Consumption - {2 * self.param + 0.3}"


coat = Coat(42)
costume = Costume(170)
print(coat.consumption)
print(costume.consumption)
