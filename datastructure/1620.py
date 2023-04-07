#---자료구조 나는야 포켓몬 마스터 이다솜 백준 1620번

# 아이디어
# N 과 M 을 입력받는다.
# Key 값은 숫자 1부터 시작한다.
# N 만큼 반복문을 돌면서 도감에 포켓몬 이름을 넣는다.
# M 만큼 반복문을 돌면서 포켓몬 이름 or 포켓몬 번호를 입력한다.
# 포켓몬 이름일 경우, 포켓몬 번호 출력 / 포켓몬 번호인 경우, 포켓몬 이름 출력

# 시간복잡도
# O(N+M)

# 자료구조
# 도감에 들어갈 포켓몬 이름 수: int N
# 도감에서 찾을 포켓몬 문제 수: int M

import sys
input = sys.stdin.readline
dict=dict()
N,M=map(int, input().split())
for i in range(1, N+1): # 도감에 들어갈 포켓몬 세팅
    name = input().rstrip()
    dict[i] = name

reverseDict = {v:k for k,v in dict.items()} # 딕셔너리의 {key, value} 를 뒤집어 저장

for _ in range(M): # 도감에서 찾을 포켓몬 문제
    pmonster = input().rstrip()
    if pmonster.isalpha(): # 입력값이 문자열(알파벳)인 경우
        print(reverseDict.get(pmonster, 0))
    else: # 입력값이 숫자인 경우
        print(dict.get(int(pmonster), 0))
