#ITP1_9_D: Transformation
#文字列 str に対して、与えられた命令の列を実行するプログラムを作成
#Write a program which performs a sequence of commands to a given string str.

str = input().lower()
q = int(input())

for i in range(q):
    n = input().split()

    s = n[0]
    a = int(n[1])
    b = int(n[2]) + 1
    
    if(s == 'replace'):
        str = str[:a] + n[3] + str[b:]
    elif(s == 'reverse'):
        str = str[:a] + str[a:b][::-1] + str[b:]
    else:
        print(str[a:b])

