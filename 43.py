#ITP1_11_C: Dice III
#Dice I と同様の方法で、入力された整数から２つのサイコロをつくります。
#これらが同一のものか判定するプログラムを作成
#Write a program which reads the two dices constructed in the same way as Dice I, and determines whether these two dices are identical.


class dice1:
    def __init__(self,label):
        self.ichi, self.ni, self.san, self.yon, self.go, self.roku = label
        
    def koro(self,i):
        if(i =='N'):
           self.ichi, self.ni, self.roku, self.go = self.ni, self.roku, self.go , self.ichi
        elif(i =='E'):
           self.ichi, self.yon , self.roku, self.san = self.yon , self.roku, self.san, self.ichi
        elif(i =='W'):
           self.ichi, self.san, self.roku, self.yon = self.san, self.roku, self.yon , self.ichi
        elif(i =='S'):
           self.ichi, self.go , self.roku, self.ni = self.go , self.roku, self.ni, self.ichi

    def print_top(self):
        print(self.ichi)

    def print_right(self):
        print(self.san)

    def glabel(self):
        return [self.ichi, self.ni, self.san, self.yon, self.go, self.roku]


label = list(map(int,input().split()))

d = dice1(label)
d2 = list(map(int,input().split()))
for i in range(1,100000000):
    if(d.glabel() == d2):
        print('Yes')
        break
    d.koro(i)
else:
    print('No')