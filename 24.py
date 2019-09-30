#ITP1_6_D: Matrix Vector Multiplication
#n×m の行列 A と、m×1 の列ベクトルb を読み込み、A と b の積を出力するプログラムを作成
#Write a program which reads a $ n \times m$ matrix $A$ and a $m \times 1$ vector $b$, and prints their product $Ab$.
n, m = map(int, input().split())

A = []
b = []

for i in range(n):
    A.append([int(s) for s in input().split()])

for i in range(m):
    b.append([int(input())])


for i in range(n):
    c = 0
    for j in range(m):
        c += A[i][j] * b[j][0]
    print(c)