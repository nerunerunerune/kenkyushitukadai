#ITP1_2_C:Sorting Three Numbers
#３つの整数を読み込み、それらを値が小さい順に並べて出力するプログラムを作成
#Write a program which reads three integers, and prints them in ascending order.
l = input().split()
a = int(l[0])
b = int(l[1])
c = int(l[2])

if(1<a,b,c and a,b,c<10000):
    a,b,c = sorted(l)
    print(a,b,c)
