# 배열 돌리기 백준 17276번

# 의사코드
import sys
input = sys.stdin.readline
# 테스트 케이스의 수 T 입력한다.
T=int(input())

def move(n, d, graph: list): # 행렬의 크기, 각도, 원소들
    n -= 1
    count = abs(d) // 45 # 돌리는 횟수
    minus = False # 시계방향 플래그
    if d < 0:
        minus = True # 반시계방향 플래그
    
    for _ in range(count):
        if not minus: # 양수 시계방향
            prev_list = list()

            for i in range(n+1): # 주 대각선
                prev_list.append(graph[i][i])
            
            for i in range(n+1): # 주 대각선 -> 가운데 열
                prev_temp = graph[i][(n+1)//2]
                graph[i][(n+1)//2] = prev_list[i]
                prev_list[i] = prev_temp
            
            for i in range(n+1): # 가운데 열 -> 부 대각선
                prev_temp = graph[i][n-i]
                graph[i][n-i] = prev_list[i]
                prev_list[i] = prev_temp
            
            for i in range(n+1): # 부 대각선 -> 가운데 행
                prev_temp = graph[(n+1)//2][n-i]
                graph[(n+1)//2][n-i] = prev_list[i]
                prev_list[i] = prev_temp
            
            for i in range(n+1): # 가운데 행 -> 주 대각선
                graph[n-i][n-i] = prev_list[i]
        else: # 음수 반시계방향
            prev_list = list()

            for i in range(n+1): # 주 대각선
                prev_list.append(graph[i][i])
            
            for i in range(n+1): # 주 대각선 -> 가운데 행
                prev_temp = graph[(n+1)//2][i]
                graph[(n+1)//2][i] == prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n+1): # 가운데 행 -> 부 대각선
                prev_temp = graph[n-1][i]
                graph[n-1][i] = prev_list[i]
                prev_list[i] = prev_temp
            
            for i in range(n+1): # 부 대각선 -> 가운데 열
                prev_temp = graph[n-i][(n+1)//2]
                graph[n-i][(n+1)//2] = prev_list[i]
                prev_list[i] = prev_temp
            
            for i in range(n+1): # 가운데 열 -> 주 대각선
                graph[n-i][n-i] = prev_list[i]

for _ in range(T):
    n,d=map(int, input().split())
    graph=[list(map(int, input().split())) for _ in range(n)]
    move(n,d,graph)
    
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=' ')
        print()
