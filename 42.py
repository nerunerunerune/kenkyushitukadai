#ITP1_11_B: Dice II
#このサイコロを Dice Iの方法で回転させた後の上面と前面の整数が質問として与えられるので、
#右側の面の整数を答えるプログラムを作成
#You are given integers on the top face and the front face after the dice was rolled 
#in the same way as Dice I. Write a program to print an integer on the right side face.


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
q = int(input())
d = dice1(label)
for x in range(q):
    uemae = [int(x) for x in input().split()]
    for i in range(1,100000000):
        if(d.glabel()[:2] == uemae):
            d.print_right()
            break
        break
    d.koro(i)