import math

a = int(input())
b = int(input())

if b <= 1:
    first = math.log(a)
    print(round(first, 2))
else:
    second = math.log(a, b)
    print("%.2f" % second)