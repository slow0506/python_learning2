import math
n = int(input())
total = math.exp(n) / (math.exp(n) + 1)
print(round(total, 2))