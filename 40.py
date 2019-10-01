#ITP1_10_D: Distance II
#２つのn次元ベクトルが与えられるので、pがそれぞれ 1、2、3、∞ のミンコフスキー距離を求めるプログラムを作成
#Write a program which reads two n dimensional vectors x and y, and calculates Minkowski's distance where p=1,2,3,∞ respectively.

n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))


p0 = [abs(i - j) for (i, j) in zip(x, y)]
for p in range(1, 4):
    d = [sum([i ** p for i in p0]) ** (1 / p)]
    print('{0:.8f}'.format(*d))
print('{0:.8f}'.format(max(*p0)))

