# 전구 백준 21918번

# 의사코드
# 1은 전구가 켜져 있는 상태
# 0은 전구가 꺼져 있는 상태

import sys
input = sys.stdin.readline

# 전구의 개수 N과 명령어의 개수 M을 입력받는다.
n,m=map(int, input().split())

# N개의 전구가 어떤 상태인지 s를 입력받는다.
# N개의 전구가 1부터 시작해 맨 앞 인덱스는 0으로 초기화해서 사용한다.
s=[0]+list(map(int, input().split()))

for _ in range(m): # 명령 개수만큼 반복한다.
    # M+2 번째 줄까지 세 개의 정수 a,b,c가 입력된다.
    a,b,c = map(int, input().split())
    # 명령 a가 1일 때, b번째 전구의 상태를 c로 변경한다.
    if a == 1:
        s[b] = c        
    # 명령 a가 2일 때, b번째 전구부터 c번째 전구까지의 상태를 변경한다. (켜져있는 전구는 끄고, 꺼져있는 전구는 킨다.)
    elif a == 2:
        for i in range(b, c+1):
            if s[i] == 0:
                s[i] = 1
            else: s[i] = 0
    # 명령 a가 3일 때, b번째 전구부터 c번째 전구까지 전구를 끈다.
    elif a == 3:
        for i in range(b, c+1):            
                s[i] = 0
    # 명령 a가 4일 때, b번째 전구부터 c번째 전구까지 전구를 킨다.
    elif a == 4:
        for i in range(b, c+1):            
                s[i] = 1
# 전구의 상태를 출력한다.
# 맨 앞 인덱스가 0이라서 1부터 n+1까지 출력한다.
for i in range(1, n+1):
    print(s[i], end=' ')
