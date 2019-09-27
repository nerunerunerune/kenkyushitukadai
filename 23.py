#ITP1_6_C: Official House
#Ａ大学は１フロア１０部屋、３階建ての公舎４棟を管理しています。
#公舎の入居・退去の情報を読み込み、各部屋の入居者数を出力するプログラムを作成
#You manage 4 buildings, each of which has 3 floors, each of which consists of 10 rooms. 
#Write a program which reads a sequence of tenant/leaver notices, and reports the number of tenants for each room.
n = int(input())

count = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]

for x in range(n):
    b, f, r, v = map(int, input().split())
    count[b-1][f-1][r-1] += v

for b in range(4):
    for f in count[b]:
        print('',*f)
    print('#'*20)