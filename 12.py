#ITP1_3_D: How Many Divisors?
#３つの整数 a,b,cを読み込み、aからbまでの整数の中に、cの約数がいくつあるかを求めるプログラムを作成
#Write a program which reads three integers a, b and c, and prints the number of divisors of c between a and b.
l = input().split()
a = int(l[0])
b = int(l[1])
c = int(l[2])

count = 0
for x in range(a,b+1):
    if(c % x == 0):
        count = count + 1  
print(count)