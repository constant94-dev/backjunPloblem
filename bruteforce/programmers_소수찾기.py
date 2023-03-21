# 소수찾기 문제 단순화하기
# 숫자 카드를 모두 조합하여 만들 수 있는 숫자 중, 소수는 몇개인가?

# 해결책
# 1. 숫자 조합: 생성 가능한 모든 숫자 조합을 만든다.
# 2. 소수가 아닌 수 제거: 숫자들의 조합 중 소수가 아닌 수를 전부 제거한다. (feat. 에라토스테네스의 체)
# 에라토스테네스의 체: 숫자 조합의 가장 큰 숫자의 루트를 씌운 값까지만 확인하면 된다.
# (ex. '71'이 가장 큰수라면 2의 배수 ~ 8의 배수까지만 제거한다.)

# Tip
# 지금 이번에 내가 해야될게 뭔지 정확히 알고
# 내가 언제 여기를 탈출해 나갈것인지
# 위 두가지만 알면 재귀가 훨씬 쉬워질 것이다.

# 의사코드로 시작한다.
# 정확한 로직을 작성하기보다 내가 만든 함수가 잘 동작한다고 가정하고 구조를 먼저 만든다.
# 위에서 부터 계속 큰 그림을 잡으면서 아래로 내려가자. (top -> down 방식)

# 1. 결과물을 담고 있을 prime_set을 정의한다.
prime_set = set()

def isPrime(number):
    # 6. '0' 과 '1'은 제외한다.
    if number in (0,1):
        return False
    
    # 7. 에라토스테네스의 체
    lim = int(number ** 0.5+1)
    for i in range(2, lim):
        if number % i == 0: # 나누어 떨어진다면 number는 i 의 배수, i는 number 의 약수이기 때문에 소수가 아니다.
            return False
    
    return True # 위 반복문을 다 돌고도 끝나지 않았다면 소수이기 때문에 True를 리턴한다.

def recursive(combination, others): # 여태까지 조합된 숫자, 아직 쓰지 않은 숫자
    # 5. 탈출 조건 / 비교 조건: 지금까지 만들어진 조합에서 소수를 찾는다
    if combination != "": # 비어있는 문자열로 들어왔을 때 int 변환을 하면 오류가 발생하니 체크!
        if isPrime(int(combination)): # 소수가 맞다면 prime_set 에 추가해준다
            prime_set.add(int(combination))

    # 4. 현재까지 만들어진 숫자에, 남아있는 숫자 중 하나를 더해준다. (내가 지금 꿈속에서 할 일)
    for i in range(len(others)):
        # others[:i] -> others 에서 i 번째 전까지 뽑은 것
        # others[i+1:] -> others 에서 i+1 번째부터 끝까지 뽑은 것
        # 내가 '1'번을 사용했다면 0번과 2번부터 끝까지
        recursive(combination+others[i], others[:i] + others[i + 1:])


def solution(numbers):    
    # 2. 모든 조합을 만드는 recursive를 수행한다.
    recursive("", numbers) # 처음 시작은 빈 문자열로 시작하지만 인자값 numbers 를 사용해

    # 3. prime_set의 length를 반환한다.    
    return len(prime_set)

print(solution("17"))
