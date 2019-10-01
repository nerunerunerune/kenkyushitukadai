#ITP1_7_D: Matrix Multiplication
#n×mの行列Aとm×lの行列Bを入力し、それらの積であるn×lの行列Cを出力するプログラムを作成
#Write a program which reads a n×m matrix A and a m×l matrix B, and prints their product, a n×l matrix C.
#An element of matrix C is obtained by the following formula.
n,m,l = map(int, input().split())

A = [list(map(int, input().split())) for i in range(n)]
B = [list(map(int, input().split())) for j in range(m)]


for i in A:
    C = []
    for j in list(map(list, zip(*B))):
       C.append(sum(s * t for s,t in zip(i, j)))

    print(*C)
