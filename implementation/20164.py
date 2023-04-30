# 지금까지 카운트된 홀수의 개수, 수가 세 자리 이상일 때 자르는 법, 재귀를 사용해 세 자리 이상 수 를 다양한 경우의 수로 조합하는 법
# 위 내용을 떠올리고 구현하는 것이 핵심!

import sys
input = sys.stdin.readline

N = input().rstrip() # 처음에 주어지는 수
makes = [] # 홀수 개수 최종값을 저장하는 리스트

def new_num_sum(num:str):
    # 숫자의 각 자리수에서 홀수의 개수를 리턴
    new_num_total = 0
    for i in num:
        if int(i) % 2 == 1: # 홀수일 때
            new_num_total += 1
    return new_num_total


def solution(n:str, total:int): # 지금 수, 지금까지 홀수의 개수
    if len(n) == 1: # 수가 한 자리일 때 종료
        makes.append(total) # 지금까지 계산된 홀수의 개수를 리스트에 추가
        return
    
    elif len(n) == 2: # 수가 두 자리일 때
        new_num = int(n[0]) + int(n[1]) # 2개로 나누고, 더해서 새로운 수로 생각하기
        solution(str(new_num), total + new_num_sum(str(new_num))) # 수가 한 자리가 될 때까지 재귀호출
    
    else: # 수가 세 자리 이상일 때
        for i in range(1, len(n)): # 자를 위치 2개
            for j in range(i+1, len(n)):
                part1 = n[:i] # 첫번째 잘린 수, i번째 전까지
                part2 = n[i:j] # 두번째 잘린 수, i부터 j번째 전까지
                part3 = n[j:] # 세번째 잘린 수, j부터 마지막까지

                new_num = int(part1) + int(part2) + int(part3) # 3개의 수로 나누고, 더해서 새로운 수로 생각하기
                solution(str(new_num), total + new_num_sum(str(new_num))) # 수가 한 자리가 될 때까지 재귀호출

solution(N, new_num_sum(N))
print(min(makes), max(makes))
