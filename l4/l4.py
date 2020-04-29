import w1

# 1
print(w1.show_msg(2, 4, 60))

# 2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")

# 3
list_ar = [el for el in range(33, 444) if el % 20 == 0 or el % 21 == 0]
print(list_ar)

# 4
from random import randint

my_list2 = [randint(-10, 10) for i in range(20)]
my_list3 = [el for el in my_list2 if my_list2.count(el) == 1]
print(f"Source list\n{my_list2}\nNo repetition list\n{my_list3}")

# 5
from functools import reduce


def sum_list(el_1, el_2):
    return el_1 * el_2


uniq_list = [el for el in range(100, 1001, 2)]
print(f"List\n{uniq_list}\nMultiplication of numbers\n{reduce(sum_list, uniq_list)}")

# 6
from itertools import count, cycle

print('Для генерации следующего числа необходимо нажать Enter,'
      ' для выхода из программы - "s"')
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    ent = input()
    if ent == 's':
        break

print(
    'Для генерации следующего повторения необходимо нажать Enter. Для выхода из программы введите "s"')
m_list = input('Введите список, разделяя элементы пробелом: ').split()
tr = cycle(m_list)
s = None

while s != 's':
    print(next(tr), end='')
    s = input()
