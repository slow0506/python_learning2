
a = int(input())
total = a
count = 1

if a != 55:
    list_01 = []
    n = 0
    go_on = True
    while go_on:
        list_01.append(int(input()))
        if list_01[n] == 55:
            go_on = False
        else:
            total = total + list_01[n]
            count += 1
            n += 1

else:
    total = 0
    count = 0
    average = 0


print(count)
print(total)
print(round(total / count))
