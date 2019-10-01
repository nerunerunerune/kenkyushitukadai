#ITP1_11_A: Dice I
#次の展開図から得られるサイコロを転がすシミュレーションを行うプログラムを作成
#Write a program to simulate rolling a dice, which can be constructed by the following net.

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


label = list(map(int,input().split()))
i_list = list(input())
d = dice1(label)
for i in i_list:
    d.koro(i)
d.print_top()
