import math
num_list = []
sqr_total = 0
n = 0
total = 0
while True:
    num_list.append(int(input()))
    if num_list[0] == 0:
        print(0)
        break

    total = total + num_list[n]
    n = n + 1
    if total == 0:
        for i in num_list:
            sqr_total = sqr_total + i ** 2
        print(sqr_total)
        break
