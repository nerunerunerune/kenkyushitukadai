#ITP1_7_A: Grading
#あるクラスの数学の成績を付けるプログラムを作成
#Write a program which reads a list of student test scores and evaluates the performance for each student.

while True:
    m, f, r = map(int, input().split())
    g = m + f
    if(m == f == r == -1):
        break
    elif(m == -1 or f == -1):
        print('F')
    elif(g >= 80):
        print('A')
    elif(g >= 65 and g < 80):
        print('B')
    elif((g >= 50 and g < 65) or (g >= 30 and r >= 50)):
        print('C')
    elif(g >= 30 and g < 50):
        print('D')
    else:
        print('F')