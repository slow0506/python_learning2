import math
angle = int(input())
x = math.radians(angle)
c = math.cos(x)
s = math.sin(x)
print(round(c/s, 10))