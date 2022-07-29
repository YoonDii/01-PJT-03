import sys

sys.stdin = open("_소득불균형.txt")

t = int(input())

for i in range(1,t+1):
    n = int(input())
    money = list(map(int,input().split()))
    total = sum(money)
    m_arg = (total // n)
    #print(money,total,m_arg)

    people = 0
    for x in money :
        if x <= m_arg :
            people += 1
    print(f'#{i} {people}')