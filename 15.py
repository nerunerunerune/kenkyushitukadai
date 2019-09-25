#ITP1_4_C: Simple Calculator
#２つの整数 a, b と１つの演算子 op を読み込んで、a op b を計算するプログラムを作成
#ただし、演算子 op は、"+"(和)、"-"(差)、"*"(積)、"/"(商)、のみとし、
#割り算で割り切れない場合は、小数点以下を切り捨てたものを計算結果とする。
#Write a program which reads two integers a, b and an operator op, and then prints the value of a op b.

num = 1
while True:
    a, op, b = input().split()   # 3変数ともに文字列として読み込む
    a = int(a)                   # a を整数に変換
    b = int(b)                   # b を整数に変換
    if(0<=a, b<=20000):
        if op == "+":
            c = a + b
        elif op == "-":
            c = a - b
        elif op == "*":
            c = a * b
        elif op == "/":
            c = a // b

        else:
            break

    print(c)
    num = num + 1