#ITP1_10_C: Standard Deviation
#n 人の学生を含むクラスでプログラミングの試験を行った。
#それぞれの得点をs1, s2 ... snとしたときの、標準偏差を求めるプログラムを作成
#You have final scores of an examination for n students. Calculate standard deviation of the scores s1, s2 ... sn.

while True:
    n = float(input())
    if(n == 0):
        break

    s = list(map(float,input().split()))
    m = sum(s) / n

    a2 = sum([(x - m) ** 2 for x in s]) / n
    print('{0:.8f}'.format(a2 ** 0.5))
    