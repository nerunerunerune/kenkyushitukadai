#ITP1_9_C: Card Game
#太郎と花子の手持ちのカードの情報を読み込み、ゲーム終了後のそれぞれの得点を出力するプログラムを作成
#Write a program which reads a sequence of cards Taro and Hanako have and reports the final scores of the game.

n = int(input())
taro = 0
hanako = 0

for i in range(n):
    taro_card, hanako_card = input().split()

    if(taro_card > hanako_card):
        taro += 3
    elif(taro_card < hanako_card):
        hanako += 3
    else:
        taro += 1
        hanako += 1
    print(taro,hanako)
