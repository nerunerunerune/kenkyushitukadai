#ITP1_7_B: How many ways?
#1からnまでの数の中から、重複無しで３つの数を選び、それらの合計がxとなる組み合わせの数を求めるプログラムを作成
#Write a program which identifies the number of combinations of three integers which satisfy the following conditions.

while True:
    n,x = map(int, input().split())
    if(n == x == 0):
        break
    ans = 0
    for i in range(1,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                if(i + j + k == x):
                    ans += 1
    print(ans)