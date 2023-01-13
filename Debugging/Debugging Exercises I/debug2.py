import math

a = 548 # 1
b = 753 # 2
c = 162784 # -3

delta = b * b - 4 * a * c
print("Delta:", delta)

s1 = (-b - math.sqrt(delta)) / (2 * a)
s2 = (-b + math.sqrt(delta)) / (2 * a)

print("Solution 1: x = ", s1)
print("Solution 2: x = ", s2)
