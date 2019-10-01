#ITP1_9_A: Finding a Word
#１つの単語Wと文章Tが与えられます。Tの中にあるWの数を出力するプログラムを作成
#Write a program which reads a word W and a text T, and prints the number of word W which appears in text T

W = input().lower()
if(len(W)>10):
    exit()

count = 0
while True:
    T = input()
    if(T == 'END_OF_TEXT'):
        break
    count += T.lower().split().count(W)

print(count)