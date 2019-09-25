#ITP1_3_B:   Print Test Cases
#１つの整数 x を読み込み、それをそのまま出力するプログラムを作成
#Write a program which reads an integer x and print it as is.
#Note that multiple datasets are given for this problem.
num = 1
while True:
    x = int(input())
    if x == 0:
        break
    print("Case {0}: {1}".format(num,x))
    num = num + 1
