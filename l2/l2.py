#  -------------------------------------------------------- 1 ----------------------------------------------------------


my_list = [1, -2, False, 3.4, "Help", [1, 2, 3]]
p = dict()

for n in range(len(my_list)):
    p[n] = type(my_list[n])

print(p)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_list = [(-1 + 0j), 1, 2.2, True, None, 'String', [3, 4], (5, 6, 6.5), {7: 'seven', 8: 'eight'}, {9, 10}, frozenset(),
           range(11), (b'twelve'), bytearray(b'thirteen'), zip(*[(14, 15), (16, 17), ('a', 'b')]), TypeError]

for i, item in enumerate(my_list):
    print(f"{i}) {item} - {type(item)}")

#  -------------------------------------------------------- 2 ----------------------------------------------------------


my_list = list(input("Enter the numbers with out space - "))

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


a = input('Введите элементы для массива разделяя их пробелами: ').split()
i = 0
print(f'Оригинальный список {a}')
while i + 1 < len(a):
    if i % 2 == 0:
        a.insert(i, a.pop(i + 1))
    i += 1
print(f'Измененный список {a}')

#  ------------------------------------------- вариант решения ---------------------------------------------------------


user_list = input("Enter the numbers with space - ").split()

for i in range(1, len(user_list), 2):
    user_list.insert(i - 1, user_list.pop(i))

print(user_list)

#  -------------------------------------------------------- 3 ----------------------------------------------------------


month = int(input("Введите интересующий вас месяц года от 1 до 12:"))

month_dict = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август",
              9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}

month_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь",
              "ноябрь", "декабрь"]

for key in month_dict:
    if key == month:
        print(f"{month}-й месяц года - это {month_dict[key]}")
        print(f"{month}-й месяц года - это {month_list[month - 1]}")

print(f"Вы ввели не корректный месяц - {month}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


# Реализация через dict.
month = int(input('Введите номер месяца: '))
while month < 0 or month > 12:
    month = int(input('Неверно, введите номер месяца: '))

seasons = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer',
           8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
print(seasons[month])

# Реализация через list.
month = int(input('Введите номер месяца: '))
while month < 0 or month > 12:
    month = int(input('Неверно, введите номер месяца: '))
seasons = ('winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn',
           'autumn', 'autumn', 'winter')
print(seasons[month - 1])

#  -------------------------------------------------------- 4 ----------------------------------------------------------


string = (input("Enter the numbers with space - ")).split()
print(string)

for i in range(len(string)):
    if len(string[i]) <= 10:
        print(i, string[i])
    else:
        print(i, (string[i])[:10])

#  ------------------------------------------- вариант решения ---------------------------------------------------------


string = (input("Enter the numbers with space - ")).split()

for n, i in enumerate(string):
    print(n + 1, i) if len(i) <= 10 else print(n, (i[:10]))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_string = input('Введите строку из нескольких слов, разделенных пробелами: ').split()

for i, word in enumerate(my_string, 1):
    print(f'{i} {word[:10]}')

#  -------------------------------------------------------- 5 ----------------------------------------------------------


my_list = [4, 3, 3, 2, 1]

while True:
    print(f"Current rating: {my_list}")
    number = input("Enter rating number or 111 to finish - ")
    if number.lstrip('-').isdigit() and number != "111":
        number = int(number)
        if my_list.count(number):
            my_list.insert(my_list.index(number) + my_list.count(number), number)
        else:
            param = 0
            n_param = 0
            for n, i in enumerate(my_list):
                if number > i:
                    if param < i:
                        param = i
                        n_param = n
                else:
                    n_param = n + 1
            my_list.insert(n_param, number)
    elif not number.isdigit():
        print("Enter number please")
    else:
        break

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_list = [9, 8, 7, 7, 7, 6, 5, 3, 3, 3, 2, 1]
new_number = int(input("Введите новый элемент рейтинга в виде натурального числа: "))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
my_list.insert(i, new_number)
print(my_list)

#  ------------------------------------------- вариант решения ---------------------------------------------------------

my_list = [7, 5, 3, 3, 2]

n = int(input('количество ввода: '))
for it in range(n):
    number = int(input('введите рейтинг: '))
    i = 0
    for val in my_list:
        if number > val:
            break
        i += 1
    my_list.insert(i, float(number))
    print(my_list)

#  -------------------------------------------------------- 6 ----------------------------------------------------------


goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        _ = input(f'Введите значение свойства "{f}": ')  # Ввод свойства
        features[f] = int(_) if (f == 'цена' or f == 'количество') else _  # Меняем тип числовых свойства
        analytics[f].append(features[f])  # Добавляем свойство в аналитику
    goods.append((num, features))  # Добавляем свойство в список товаров
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')
    print("*" * 30)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


i = 1
database = []
analytics = []
list_ = dict()

while True:
    start = input("Hi! I'm a database of goods. If you want to continue, enter 1. Finish - 0.\n -- ")
    if start == "0":
        l = []
        print("Do you want to do analytics?")
        answer = input("Yes - y, No - n ")
        while answer == "y":
            type_ = input("Enter analytics parameter: name, price, number, units - ")
            for j in range(len(database)):
                l.append(analytics[j].get(type_))
                list_[type_] = l
            answer = input("Do you want continue? Yes - y, No - n ")
        if answer == "n":
            if database:
                print(database)
            else:
                print("You have left the program")
        else:
            print("You mast enter 'y' or 'n'")
        print(database)
        print(list_)
        break
    elif start == "1":
        good_ = dict()
        good_["name"] = input("Enter name of good - ")
        good_["price"] = input("Enter price of good - ")
        good_["number"] = input("Enter number of good - ")
        good_["units"] = input("Enter units of good - ")
        database.append((i, good_))
        analytics.append(good_)
        i += 1
    else:
        print("You didn't enter the required numbers - 0 or 1.")

#  ------------------------------------------- вариант решения ---------------------------------------------------------

enter = ''
goods = []
i = 0

while enter == '':  # если нажата клавиша Enter - вводим данные, иначе выходим
    i += 1

    name = input('\nEnter name of good: ')
    price = input('Enter price: ')
    num = input('Enter quantity of good: ')
    unit = input('Enter unit: ')

    goods.append((i, {'name': name, 'price': price, 'num': num, 'unit': unit}))
    print('\n', goods)

    enter = input('\nPress Enter for continue, any key+Enter to exit...')

# вывод "аналитики"
while True:
    print('\nChoose action: ')
    print(' [1] Print list of goods.')
    print(' [2] Print list of prices.')
    print(' [3] Print quantities.')
    print(' [4] Print units.')
    print(' [5] Exit.')

    action = input('\nYour choice: ')
    if action == '5':
        break

    names = ('Goods', 'Prices', 'Quantities', 'Units')
    titles = ('name', 'price', 'num', 'unit')
    res = {'name': [], 'price': [], 'num': [], 'unit': set()}

    for id, v in goods:
        res['name'].append(v['name'])
        res['price'].append(v['price'])
        res['num'].append(v['num'])
        res['unit'].add(v['unit'])

    print(res)

    print(f'\n{names[int(action) - 1]}: {res[titles[int(action) - 1]]}')

print('\nGoodbye!')
