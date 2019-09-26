#ITP1_5_D: Structured Programming
#C++言語のプログラムと同じ動作をするプログラムを作成
#Write a program which does precisely the same thing as the following program (this example is wrtten in C++).
#Let's try to write the program without goto statements.
n = int(input())
list = []

for i in range(3,n+1):
    if( i % 3 == 0):
        list.append(i)
    else:
        j = i
        while(j):
            if(i % 10 == 3):
                list.append(i)
                break
            else:
                j = j//10
print("",*list)
