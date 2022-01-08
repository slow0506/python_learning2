ff = []
while True:
    n = input()
    if n == ".":
        break
    else:
        ff.append(float(n))

ff.sort()
print(ff[0])
