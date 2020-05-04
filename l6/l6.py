# 1
class TrafficLight:
    __color = ("red", "yellow", "green")

    def running(self):
        print(f"Запущен {self.__color[1]}")


a = TrafficLight()
print(f"{a.running()}")


# 2
class Road:
    __r_length = 20
    __r_width = 10

    def road_method(self):
        return __r_length * __r_width


road_var = Road()
print(road_var)


# 3
class Worker:
    name = 11
    surname = 22
    position = 33
    get_total_income = 44
    __income_sl = {"wage": 11, "bonus": 22}
    income = __income_sl


class Position(Worker):
    def get_full_name(self):
        print("get_full_name")

    def get_total_income(self):
        print("get_total_income")


work = Worker()
print(work)


# 4
class Car:
    speed = 0
    color = "col"
    name = "name"
    is_police = "is_police"


def go():


def stop():


def turn(direction):


def show_speed():


# 5
class Stationery:
    title = "title"

    def draw(self):

class Pen(Stationery):

class Pencil(Stationery):

class Handle(Stationery):
