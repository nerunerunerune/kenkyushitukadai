#ITP1_11_D: Dice IV
#Dice I と同様の方法で、入力された整数から n 個のサイコロをつくります。
#これらのサイコロが、全て異なるものかどうかを判定するプログラムを作成
#Write a program which reads $n$ dices constructed in the same way as Dice I, and determines whether they are all different. 

class dice1:
    def __init__(self,label):
        self.ichi, self.ni, self.san, self.yon, self.go, self.roku = label
        
    def koro(self,i):
        if(i =='N'):
           self.ichi, self.ni, self.roku, self.go = self.ni, self.roku, self.go, self.ichi
        elif(i =='E'):
           self.ichi, self.yon, self.roku, self.san = self.yon, self.roku, self.san, self.ichi
        elif(i =='W'):
           self.ichi, self.san, self.roku, self.yon = self.san, self.roku, self.yon, self.ichi
        elif(i =='S'):
           self.ichi, self.go, self.roku, self.ni = self.go, self.roku, self.ni, self.ichi

    def print_top(self):
        print(self.ichi)

    def print_right(self):
        print(self.san)

    def glabel(self):
        return [self.ichi, self.ni, self.san, self.yon, self.go, self.roku]

    def icchi(self, label):
        for i in range(1,10000000):
            if self.glabel() == label:
                return True
            self.koro(i)
        else:
            return False

if __name__=='__main__':
    n = int(input())
    t = []
    for i in range(n):
        label = list(map(int,input().split()))
        #d = dice1(label)
        #d2 = list(map(int,input().split()))
        for d in t:
            if d.icchi(label):
                break
        else:
            t.append(dice1(label))
            continue
        print('No')
        break
    else:
        print('Yes')
