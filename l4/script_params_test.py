from random import randrange

count = 0
count_num1 = 0
count_num2 = 0

while count < 100000:
    rand_num = randrange(1, 3)
    count += 1
    if rand_num == 1:
        count_num1 += 1
        # print(f"count_num1 = {rand_num}")
    elif rand_num == 2:
        count_num2 += 1
        # print(f"count_num2 = {rand_num}")
print(f"===============================")
print(f"count_num1 = {count_num1}")
print(f"count_num2 = {count_num2}")