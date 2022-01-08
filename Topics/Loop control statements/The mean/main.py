
n_list = []
count = 0
total = 0
go_on = True
while go_on:
    n_list.append((input()))
    if n_list[0] == ".":
        print(0)
        go_on = False
        break
    if n_list[count] == ".":
        go_on = False
        break
    else:
        total += int(n_list[count])
        count = count + 1

print(total/count)