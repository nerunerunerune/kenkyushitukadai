#ITP1_8_B: Sum of Numbers
#与えられた数の各桁の和を計算するプログラムを作成
#Write a program which reads an integer and prints sum of its digits.
while True:
    n = input()
    if n == '0':
        break
    else:
        t = map(int,n)
        print(sum(t))