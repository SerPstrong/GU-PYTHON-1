# 1
int_var = int(15)
n_1 = complex(5, 6)
my_str = "простая строка"
tuple_var = (1, 2, 3, 4, 5)
abanchof = {400, None, "text", True}
list_var = list("1 fr 23 f")
my_dict = dict(key_1='val_1', key_2='val_2')
bool_var = bool()
bytes_var = bytes([10, 20, 30, 40])
none_var = None

list_arr = [int_var, n_1, my_str, tuple_var, abanchof, list_var, my_dict,
            bool_var, bytes_var, none_var]

print(type(list_arr[1]))

for el in list_arr:
    print(type(el))

# 2
list_arr_reverse = []
for item in list_var:
    if list_arr_reverse[item] == 3:
        list_arr_reverse.append(item)

print(list_var)
print(list_arr_reverse)

# 3
month = int(input("Введите номер месяца: "))
month_list = list("январь", "февраль")
month_dict = {'python': 1991, 'java': 1995, 'c++': 1983}
for el in month_list:
    print(el)

print(sorted(month_dict))
print(month_list[1])


# 4
str_input = input("Введите предложение: ")
for el in str_input:
    print(el)
