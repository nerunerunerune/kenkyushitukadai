#ITP1_5_A: Print a Rectangle
#たてH cm よこ W cm の長方形を描くプログラムを作成。1 cm × 1cm の長方形を '#'で表す。
#Draw a rectangle which has a height of H cm and a width of W cm. Draw a 1-cm square by single '#'.

while True:
    H,W = map(int, input().split())
   
    if (H == 0 and W == 0):
            break
    for j in range(H):
        for i in range(W):
            print("#", end="")
        print()
    print()