#ITP1_9_B: Shuffle
#カードの山の最初の並び（文字列）とhの列を読み込み、最後の並び（文字列）を出力するプログラムを作成
#Write a program which reads a deck (a string) and a sequence of h, and prints the final state (a string).

while True:
    n = input()
    if((n == '-') or (len(n) > 10)):
        break
    m = int(input())

    for i in range(m):
        h = int(input())
        n = n[h:] + n[:h]
    print(n)

