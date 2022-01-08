scores = input().split()
count = 0
got = 0

for n in scores:
    if n == "I":
        count = count + 1
        if count ==3:
            print("Game over")
            print(got)
            break
    else:
        got = got + 1

if count < 3:
    print("You won")
    print(got)