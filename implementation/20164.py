# 홀수 홀릭 호석 백준 20164번

#의사코드

# 호석이가 처음 시작할 때 가지고 있는 수를 입력한다.

# 수의 각 자리 숫자 중에서 홀수의 개수를 카운팅한다.

# 수가 세 자리 이상이면 임의의 위치에서 끊어서 3개의 수로 분할하고,
# 3개를 더한 값을 새로운 수로 생각한다.
# 수의 개수가 세 자리 이상이면서 홀수이면 2개씩 나눈 수들과 나머지 한 수를 더해준다.
    
# 수의 개수가 세 자리 이상이면서 짝수이면 2개씩 나눈 수들을 더해준다.

    # 더해진 수를 하나씩 비교해서 2로 나눈 나머지가 1이라면 카운팅한다.

# 수가 두 자리이면 2개로 나눠서 합을 구하여 새로운 수로 생각한다.
# 2개로 나눠진 수를 더해준다.

    # 더해진 수를 하나씩 비교해서 2로 나눈 나머지가 1이라면 카운팅한다.

# 수가 한 자리이면 더 이상 아무것도 하지 못하고 종료한다.
    

# 호석이가 만들 수 있는 최종값 중 최솟값과 최댓값을 순서대로 공백으로 구분하여 출력한다.

import sys
input = sys.stdin.readline

def new_num_sum(num:int):
    """
    숫자의 각 자리수에서 홀수의 개수를 리턴한다
    """
    new_num_total = 0
    while num:
        if (num % 10) % 2: # 한자리씩 비교하면서 홀수를 찾는다
            new_num_total += 1   
        num//=10
    return new_num_total


def sol(n: str, total: int): # 지금 수, 지금까지 홀수의 개수
    if len(n) == 1: # 수가 한 자리이면 종료
        makes.append(total) # 그때까지의 홀수의 개수를 리스트에 추가
        return

    elif len(n) == 2: # 수가 두 자리이면
        new_num = int(n[0]) + int(n[1]) # 2개로 나누고, 더해서 새로운 수로 생각하기
        sol(str(new_num), total + new_num_sum(new_num))

    else: # 수가 세 자리 이상이면
        for i in range(1, len(n)): # 자를 위치 2개
            for j in range(i+1, len(n)):
                part1 = n[:i]
                part2 = n[i:j]
                part3 = n[j:]

                new_num = int(part1) + int(part2) + int(part3) # 3개의 수로 나누고, 더해서 새로운 수로 생각하기
                sol(str(new_num), total + new_num_sum(new_num))

N = input()
makes =[]
sol(N, new_num_sum(int(N)))
print(min(makes), max(makes))
