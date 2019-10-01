#ITP1_10_B: Triangle
#三角形の２辺a, bとその間の角Cから、その三角形の面積S、周の長さL, aを底辺としたときの高さhを求めるプログラムを作成
#For given two sides of a triangle a and b and the angle C between them, calculate the following properties.
import math
a, b, C = map(int, input().split())

S = a * b * 0.5 * math.sin(math.pi * C / 180)
L = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.pi * C / 180))
h = S * 2 / a
print(S)
print(L)
print(h)