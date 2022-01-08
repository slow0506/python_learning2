n = int(input())
if n == 1:
    print(1)
else:
    total = n
    while n >= 2:
        n = n-1
        total = total * n
    print(total)
