import sys
input_fn = sys.stdin.readline

def solution(n:int, x:int):
    for i in range(n): # 1~N까지 반복하면서 분해합을 구한다
        nums = list(map(int, str(i)))
        if n == sum(nums) + i:
            x = i
            break
        if i == n:
            return 0
    return x

N=int(input_fn()) # 분해합을 입력값으로 받는다
x=0
print(solution(N,x))
