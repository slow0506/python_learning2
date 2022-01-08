guest = []
n = 0
go_on = True
guest.append(input())

if guest[0] == ".":
    go_on = False

while go_on:
    guest.append(input())
    n = n + 1
    if guest[n] == ".":
        go_on = False
        guest.pop(n)


print(guest)
print(n)


