import sys

sys.stdin = open("_직사각형길이찾기.txt")



t = int(input())

for i in range(1, t+1):
    num = list(map(int,input().split())) 

    d = 0 #남은변길이
    if num.count(num[0]) == 3 : # 3개 수가 똑같으면 d도 같은 수
        d = num[0]  
    else :
        if num.count(max(num)) == 1 : # 최댓값이 1개라면 d도 최댓값
            d = max(num) 
        else :                         #최댓값이 2개라면 d는 최솟값
            d = min(num)
    print(f'#{i} {d}')
