#ITP1_10_A: Distance
#２点 P1(x1, y1), P2(x2, y2) の距離を求めるプログラムを作成
#Write a program which calculates the distance between two points P1(x1, y1) and P2(x2, y2).
import math
x1, y1, x2, y2 = map(float, input().split())

print('{0:8f}'.format(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)))
