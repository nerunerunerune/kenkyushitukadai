#ITP1_4_B: Circle
#半径 r の円の面積と円周の長さを求めるプログラムを作成
#Write a program which calculates the area and circumference of a circle for given radius r.

import math
pi = math.pi
r = float(input())

if(0<r<10000):
    S = r * r * pi
    E = 2 * r * pi

    print("{0:.6f} {1:.6f}".format(S,E))