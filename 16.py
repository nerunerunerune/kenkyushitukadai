#ITP1_4_D:   Min, Max and Sum
#n  個の整数 ai(i=1,2,...n)を入力し、それらの最小値、最大値、合計値を求めるプログラムを作成
#Write a program which reads a sequence of n integers ai(i=1,2,...n), and prints the minimum value,
#maximum value and sum of the sequence.
n = input()
lst = list(map(int, input().split()))


a = min(lst)
b = max(lst)
c = sum(lst)

print(a,b,c)
