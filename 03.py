# ITP1_1_C: Rectangle
#たて a cm よこ b cm の長方形の面積と周の長さを求めるプログラム
#Write a program which calculates the area and perimeter of a given rectangle.
l = input().split()
a = int(l[0])
b = int(l[1])

if(1<=a & b<=100):
    print(a*b, 2*(a+b))
