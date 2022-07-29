import sys

sys.stdin = open("_문자열의거울상.txt")

t = int(input())

for i in range(1,t+1):
    n = list(input())

    nl = len(n) 
    mir = ''
    for x in range(nl): #글자를 하나하나 나눠서 생각하기.
        word = str(n[-1 - x])
        #print(word)
        if word == 'p':
            mir += 'q'
        elif word == 'q':
            mir += 'p'
        elif word == 'b':
            mir += 'd'
        else:
            mir += 'b'
    print(f'#{i} {mir}') 
