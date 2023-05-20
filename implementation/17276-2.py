import sys
input_fn = sys.stdin.readline

def turn45(n:int, d: int, graph: list):
    n -= 1 # 입력받은 행렬의 크기의 1을 뺀다. 이유는 내가 사용할 행렬은 [4][4] 까지라서
    count = abs(d) // 45 # d 가 음수 or 양수라서 절대값으로 d 를 확인한다.
    minus = False # 시계방향
    if d < 0:
        minus = True # 반시계방향
    
    for _ in range(count): # 45도 회전 횟수
        if not minus: # 양수일 때, 기본값이 False 라서 not 하면 True 가 들어온다
            prev_list = list() # 이동 전 그래프 보관용

            for i in range(n+1): # 인덱스 0~4 까지 반복, 주 대각선 구성                
                prev_list.append(graph[i][i])
                
            for i in range(n+1): # 1. 주대각선 -> 가운데열                
                prev_temp = graph[i][(n+1)//2] # 가운데 열 값을 보관
                graph[i][(n+1)//2] = prev_list[i] # 주 대각선 값을 가운데 열로 변경
                prev_list[i] = prev_temp # 보관한 가운데 열 값으로 새롭게 구성
                
            for i in range(n+1): # 2. 가운데열 -> 부대각선
                prev_temp = graph[i][n-i] # 부 대각선 값을 보관
                graph[i][n-i] = prev_list[i] # 가운데 열 값을 부 대각선으로 변경
                prev_list[i] = prev_temp # 보관한 부 대각선 값으로 새롭게 구성
                
            for i in range(n+1): # 3. 부대각선 -> 가운데행
                prev_temp = graph[(n+1)//2][n-i] # 가운데 행 값을 보관
                graph[(n+1)//2][n-i] = prev_list[i] # 부 대각선 값을 가운데 행으로 변경
                prev_list[i] = prev_temp # 보관한 가운데 행 값으로 새롭게 구성

            for i in range(n+1): # 4. 가운데행 -> 주대각선
                graph[n-i][n-i] = prev_list[i] # 다음 조건이 없어 보관한 값을 바로 대입
        else: # 음수일 때,
            prev_list = list()

            for i in range(n+1): # 주 대각선 구성
                prev_list.append(graph[i][i])

            for i in range(n+1): # 주 대각선 -> 가운데 행
                prev_temp = graph[(n+1)//2][i] # 가운데 행 값을 보관
                graph[(n+1)//2][i] = prev_list[i] # 주 대각선 값을 가운데 행으로 변경
                prev_list[i] = prev_temp # 보관한 가운데 행 값으로 새롭게 구성
                
            for i in range(n+1): # 가운데 행 -> 부 대각선
                prev_temp = graph[n-i][i] # 부 대각선 값을 보관
                graph[n-i][i] = prev_list[i] # 가운데 행 값을 부 대각선으로 변경
                prev_list[i] = prev_temp # 보관한 부 대각선 값으로 새롭게 구성

            for i in range(n+1): # 부 대각선 -> 가운데 열
                prev_temp = graph[n-i][(n+1)//2] # 가운데 열 값을 보관
                graph[n-i][(n+1)//2] = prev_list[i] # 가운데 열값을 부 대각선으로 변경
                prev_list[i] = prev_temp # 보관한 가운데 열 값으로 새롭게 구성

            for i in range(n+1): # 가운데 열 -> 주 대각선
                graph[n-i][n-i] = prev_list[i] # 다음 조건이 없어 보관한 값을 바로 대입

def solution(T: int):    
    for _ in range(T):
        n, d = map(int, input_fn().split())
        graph = [list(map(int, input_fn().split())) for _ in range(n)]
        
        turn45(n, d, graph) # 조건에 맞게 배열을 돌리기를 수행하는 함수

        for i in range(n):
            for j in range(n):
                print(graph[i][j], end=' ') # 요소마다 한 칸의 공백을 줄거다
            print() # 한 행의 요소가 출력되면 한 줄을 넘어간다 (Enter)
t = int(input_fn())
solution(t)
