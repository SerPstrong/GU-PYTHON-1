# 1
def my_sum(arg_1, arg_2):
    return arg_1 / arg_2


print(my_sum(20, 30))


# 2
def func_name(arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, ):
    return arg_1 + arg_2 + arg_3 + arg_4 + arg_5 + arg_6


print(func_name("Ivan ", "Ivanov ", "1967 ", "Tagil ", "mail@m.ru ", "+7 (111) - 235 - 42 - 34"))


# 3
def func_max_sum(arg_1, arg_2, arg_3):
    if arg_1 > arg_2 and arg_1 > arg_3 or arg_2 > arg_3:
        return arg_1 + arg_2
    elif arg_2 > arg_1 and arg_2 > arg_3 or arg_3 > arg_1:
        return arg_2 + arg_3
    else:
        return arg_3 + arg_1


print(func_max_sum(4, 6, 8))


# 4
def func_pow(x, y):
    return x ** y


print(func_pow(2, 8))


# 5


def func_input_sum(x):
    x = x.split()
    b = []
    for i in x:
        b.append(int(i))
    return sum(b)


s = 0
while 1:
    x = input("Введите числа разделенные пробелами. Для завершения введите s: ")
    if x == "s":
        break
    s += func_input_sum(x)
    print('Сумма чисел:', s)


# 6
def int_func(word):
    return word.title()


print(int_func("text sdrgsdr argarad"))
