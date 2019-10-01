#ITP1_7_C: Spreadsheet
#表計算を行う簡単なプログラムを作成
#Your task is to perform a simple table calculation.

r,c = map(int, input().split())
lst = [list(map(int, input().split())) for i in range(c)]

for i in range(r):
    lst[i].append(sum(lst[i]))

lst.append(list(map(sum, zip(*lst))))


for j in lst:
    print(*j)