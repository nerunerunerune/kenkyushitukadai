#ITP1_4_A:  A / B Problem
#２つの整数 a と b を読み込んで、以下の値を計算するプログラムを作成
#Write a program which reads two integers a and b, and calculates the following values.
l = input().split()
a = int(l[0])
b = int(l[1])

if (1<=a,b<=10^9):
    d = a // b
    r = a % b
    f = a / b

    print("{0} {1} {2:.5f}".format(d, r, f))  
