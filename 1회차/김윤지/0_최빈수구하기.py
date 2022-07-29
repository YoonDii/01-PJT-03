import sys

sys.stdin = open("_최빈수구하기.txt")

t = int(input())

for i in range(t):
    tc = int(input())
    grd = list(map(int,input().split())) #점수
    m = 0 #최빈수값

    m_dict = {} #최빈수 딕셔너리
    for i in grd:
        if i in m_dict: # i가 있으면 1씩 더하기
            m_dict[i] += 1
        else:           # 아니면 그대로
            m_dict[i] = 1
#print(m_dict)

    max_m = 0 #최빈수 딕셔너리에서 숫자값(k)과 카운트한 값(v)로 더 큰 점수 구하기/최댓값구하기
    for k , v in m_dict.items():
        if max_m < v: #만약 v가 최댓값이면 최빈수(m)을 k에 넣는다.
            max_m = v
            m = k
                
        elif max_m == v : # 최댓값과 v가 같으면 더 큰 점수 가져오기
            if m < k:
                m = k
    print(f'#{tc} {m}')   
