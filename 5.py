#ITP1_2_A: Small, Large, or Equal
#２つの整数 a, b を読み込んで、a と b の大小関係を出力する
#Write a program which prints small/large/equal relation of given two integers a and b.
l = input().split()
a = int(l[0])
b = int(l[1])

if(-1000<=a & b<=1000):
    if(a<b):
        print("a < b")
    elif(a>b):
        print("a > b")
    elif(a==b):
        print("a == b")