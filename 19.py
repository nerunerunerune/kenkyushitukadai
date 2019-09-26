#ITP1_5_C: Print a Chessboard
#たてH cm よこ W cm のチェック柄の長方形を描くプログラムを作成
#Draw a chessboard which has a height of H cm and a width of W cm.
#For example, the following figure shows a chessboard which has a height of 6 cm and a width of 10 cm.
while True:
    H,W = map(int, input().split())
   
    if (H == 0 and W == 0):
            break
    for j in range(H):
        for i in range(W):
            print('#.'[(i+j) % 2] , end="")
        print()
    print()