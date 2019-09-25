#ITP1_2_B: Range
#３つの整数a, b, cを読み込み、それらが a < b < cの条件を満たすならば"Yes"を、満たさないならば"No"を出力
#Write a program which reads three integers a, b and c, and prints "Yes" if a<b<c, otherwise "No".
l = input().split()
a = int(l[0])
b = int(l[1])
c = int(l[2])

if(0<=a and c<=100):
    if(a<b<c and 0<=a and c<=100):
        print("Yes")
    else:
        print("No")
