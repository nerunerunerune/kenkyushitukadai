#ITP1_8_C: Counting Characters
#与えられた英文に含まれる、各アルファベットの数を数えるプログラムを作成
#Write a program which counts and reports the number of each alphabetical letter.
lst = []
a = 'abcdefghijklmnopqrstuvwxyz'
b = dict.fromkeys(list(a), 0)
while True:
    n = input()
    if n == '':
        break
    lst.append(n)

    for i in n.lower():
        if i in a:
            b[i] += 1 
sorted(lst)

for i in a:
    print("{} : {}".format(i,b[i]))

