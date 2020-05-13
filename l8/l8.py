# 1
class Data:
    def date(self, day, month, year):
        return int(f"{day}+{month}+{year}")

    # def date2(self):


b = Data.date(22, 10, 2020)

print(b)


# 2


# 3


# 4
class Warehouse:
    pass


class Office_equipment:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Printer(Office_equipment):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Scanner(Office_equipment):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Copier(Office_equipment):
    def __init__(self, width, height):
        self.width = width
        self.height = height

# 5


# 6


# 7
