#ITP1_8_D: Ring
#リング状の文字列sの任意の位置から、時計回りに連続した文字をいくつか選んで、文字列pが作れるかを判定するプログラムを作成
#Write a program which finds a pattern p in a ring shaped text s.
s = input()
p = input()

if p in (s + s):
    print('Yes')
else:
    print('No')

exit()
