#ITP1_6_A: Reversing Numbers
#与えられた数列を逆順に出力するプログラムを作成
#Write a program which reads a sequence and prints it in the reverse order.
n = int(input())
lst = list(map(int, input().split()))

lst.reverse()
print(*lst)