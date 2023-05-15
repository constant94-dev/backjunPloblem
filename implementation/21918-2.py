import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = list(map(int, input().split()))
    
def solution(M, s):
    for _ in range(M):
        a, b, c = map(int, input().split())

        if a == 1:
            s[b-1] = c
            print("1번째: ",s)
        elif a == 2:
            print("2번째 시작: ", b, c)
            for i in range(b-1,c):
                if s[i] == 0:
                    s[i] = 1
                elif s[i] == 1:
                    s[i] = 0
            print("2번째: ",s)
        elif a == 3:
            for i in range(b-1,c):
                s[i] = 0                
            print("3번째: ",s)
        elif a == 4:
            for i in range(b-1,c):
                s[i] = 1
            print("4번째: ",s)       

solution(M, s)
for i in range(N):
    print(s[i], end=' ')
