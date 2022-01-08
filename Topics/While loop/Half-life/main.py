import math

big = int(input())
small = int(input())
ave = math.floor(big / 2)
count = 1
if ave >= small:
    while ave >= small:
        ave = math.floor(ave / 2)
        count +=1
    print(count * 12)
else:
    print(count * 12)