#ITP1_6_B: Finding Missing Cards
#太郎が花子と一緒にトランプ遊びをしようとしたところ、52枚あるはずのカードが n 枚のカードしか手元にありません。
#これらの n 枚のカードを入力として、足りないカードを出力するプログラムを作成
#Taro is going to play a card game. However, now he has only n cards, even though there should be 52 cards (he has no Jokers).
n = int(input())
cards = ["{0} {1}".format(j, i) for j in ('S', 'H', 'C', 'D') for i in range(1, 13 + 1)]
card = []

for x in range(n):
    card = input()
    cards.remove(card)

for i in cards:
        print(i)