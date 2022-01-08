# put your python code here
import math
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
s_2 = p*(p-a)*(p-b)*(p-c)
s = math.sqrt(s_2)
print(s)