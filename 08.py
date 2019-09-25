#ITP1_2_D:Circle in a Rectangle
#長方形の中に円が含まれるかを判定するプログラムを作成
#次のように、長方形は左下の頂点を原点とし、右上の頂点の座標 (W,H) が与えられます。
#また、円はその中心の座標 (x,y) と半径 r で与えられます。

#Write a program which reads a rectangle and a circle,
#and determines whether the circle is arranged inside the rectangle.
#As shown in the following figures, the upper right coordinate $(W, H)$ of the rectangle
#and the central coordinate $(x, y)$ and radius $r$ of the circle are given.

l = input().split()
W = int(l[0])
H = int(l[1])
x = int(l[2])
y = int(l[3])
r = int(l[4])

if(-100<=x and y<=100):
    if(0<W,H,r and W,H,r<=100):
        if(r<=x<=W-r and r<=y<=H-r):
            print("Yes")
        else:
            print("No")
