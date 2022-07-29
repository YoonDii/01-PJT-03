import sys

sys.stdin = open("_신용카드만들기1.txt")

t = int(input())
for i in range(1, t+1):
    nums = list(map(int,input().split()))
