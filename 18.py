#ITP1_5_B: Print a Frame
#たてH cm よこ W cm の枠を描くプログラムを作成
#Draw a frame which has a height of H cm and a width of W cm.
#For example, the following figure shows a frame which has a height of 6 cm and a width of 10 cm.
while True:
    H,W = map(int, input().split())
   
    if (H == 0 and W == 0):
            break
    for j in range(H):
        if(j == 0 or j == H-1):
            print('#'* W)
        else:
            print('#' + '.' * (W - 2) + '#')
    print('')
