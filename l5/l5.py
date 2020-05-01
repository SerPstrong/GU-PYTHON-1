# 1
with open('text.txt', 'w', encoding='utf-8') as file:
    while True:
        line = input('Введите строку: ')
        if not line:
            break
        print(line, file=file)

# 2
counter = 0
with open("text.txt", "r") as f_obj:
    for line in f_obj:
        counter += 1
        line_words = line.split('')
        print(line, 'Длина строки: ', len(line_words))
    print('Всего строк: ', counter)

# 3
with open("text.txt", "r") as my_file:
    s_sum = []
    less = []
    line = my_file.read().split("\n")
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        s_sum.append(i[1])

print(f"Salary less 20000 {less}. Average salary - {sum(map(float, s_sum)) / len(s_sum)}")

# 4
rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text4.txt", "a") as new_file:
    with open("text4.txt") as my_file:
        line = my_file.read().split("\n")
        for i in line:
            i = i.split(" - ")
            new_file.writelines(rus_dic[i[0]] + ' - ' + i[1] + "\n")

# 5
from random import randint

sum_el = 0
with open("text.txt", "w") as my_file:
    for i in range(100):
        el = randint(1, 100)
        sum_el += el
        my_file.write(str(el) + " ")

print(f"Sum of elements - {sum_el}")

# 6
mydict = {}
with open("text.txt") as fobj:
    for line in fobj:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        mydict[name] = name_sum
print(f"{mydict}")
