#ITP1_1_D:   Watch
#秒単位の時間 S が与えられるので、h:m:s の形式へ変換して出力してください。
#ここで、h は時間、m は 60 未満の分、s は 60 未満の秒とします。
#Write a program which reads an integer S [second] and converts it to h:m:s where h, m, s denote hours, minutes (less than 60) and seconds (less than 60) respectively.
S = int(input())
h = S // 3600
m = S % 3600 // 60
s = S % 60
if(0<=S & S<=86400):
    print(f"{h}:{m}:{s}")
