# 1
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
year = 2020 - age
height = int(input("Введите ваш рост: "))
print("Привет", name, year, "года рождения")

# 2
number = int(input("Введите кол-во секунд: "))
hour = number // 3600
minutes = (number // 60) % 60
sec = number % 60

if hour < 10 or minutes < 10 or sec < 10:
    if hour < 10 and minutes < 10 and sec < 10:
        print(f"0{hour}:0{minutes}:0{sec}")
    elif hour < 10 and minutes < 10:
        print(f"0{hour}:0{minutes}:{sec}")
    elif hour < 10 and sec < 10:
        print(f"0{hour}:{minutes}:0{sec}")
    elif minutes < 10 and sec < 10:
        print(f"{hour}:0{minutes}:0{sec}")
    elif hour < 10:
        print(f"0{hour}:{minutes}:{sec}")
    elif minutes < 10:
        print(f"{hour}:0{minutes}:{sec}")
    else:
        print(f"{hour}:{minutes}:0{sec}")
else:
    print(f"{hour}:{minutes}:{sec}")

# 3
n = input("Введите число для зад. 3: ")
n1 = int(n)
n2 = int(n + n)
n3 = int(n + n + n)
print(n1 + n2 + n3)

# 4
num = int(input("Введите число для поиска макс.: "))
num_max = num % 10
while num > 0:
    num = num // 10
    a_num = num % 10
    if a_num > num_max:
        num_max = a_num
print("Максимальное число", num_max)

# 5
revenue = int(input("Введите выручку: "))
costs = 6000
if revenue > costs:
    print("выручка больше издержек: ")
    profitability = ((revenue - costs) // (revenue / 100))
    print("Рентабельность: ", profitability, "%")
else:
    print("издержки больше выручки")
person = int(input("Введите кол-во сотрудников: "))
print("Прибыль на одного сотрудника: ", (revenue - costs) // person)

# # 6
a = 12
b = 100
i = 1
while a <= b:
    a += int(a / 100 * 10)
    print("день №", i, "=", a)
    i += 1
