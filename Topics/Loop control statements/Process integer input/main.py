in_list = []
n = 0
while True:
    in_list.append(int(input()))
    n += 1
    if in_list[n-1] > 100:
        in_list.pop(n-1)
        break

for i in in_list:
    if i >=10:
        print(i)