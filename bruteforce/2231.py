import sys
input_fn = sys.stdin.readline

def solution(n:int, result:int):
    for i in range(n): # 해당 분해합의 생성자 찾기
        nums = list(map(int, str(i))) # i의 각 자릿수를 리스트로 만든다
        print('각 자릿수 리스트: ',nums)
        result = i + sum(nums) # 분해합 = 생성자 + 각 자릿수의 합
        print('분해합: ',result)
        # i가 작은 수부터 차례대로 들어가고 처음으로 분해합과 입력값이 같을 때가 가장 작은 생성자이다
        if n == result:
            result = i # 지금 비교되는 i 값이 가장 작은 생성자 값이므로 결과 변수에 저장한다
            break
        if i == n: # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻이다
            return 0
    return result

N=int(input_fn()) # 분해합을 입력값으로 받는다
result=0 # 결과를 담을 변수
print(solution(N,result))
