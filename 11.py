#ITP1_3_C: Swapping Two Numbers
#２つの整数 x, y を読み込み、それらを値が小さい順に出力するプログラムを作成
#Write a program which reads two integers x and y, and prints them in ascending order.

num = 1
while True:
    l = input().split()
    a = int(l[0])
    b = int(l[1])
    if (a == 0 and b == 0):
        break
    print(b,a)
    num = num + 1