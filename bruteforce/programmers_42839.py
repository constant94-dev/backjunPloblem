import math # 루트 연산을 위한 라이브러리
numberSet = set() # 중복을 없애기 위한 자료구조 Set

def recur(comb: str, others: str): # 'comb' 는 여태까지 조합된 숫자, 'others' 여태까지 쓰지 않은 숫자
    # 1. 현재 조합을 set에 추가한다.
    if comb != "":
        numberSet.add(int(comb))
    # 2. 남은 숫자 중 한 개를 더 해 새로운 조합을 만든다.
    for i in range(len(others)):
        recur(comb + others[i], others[:i] + others[i+1:]) # 이전의 문자 + i번째 문자, 지금 조합의 사용한 i 번째 문자를 제외하고 나머지 문자를 전달한다

def isPrime(num: int):
    # 1. '0' 과 '1' 은 소수가 아니다.
    if num in (0, 1):
        return False
    
    # 2. 에라토스테네스의 체의 limit을 계산한다.
    lim = int(math.sqrt(num))
    
    # 3. 에라토스테네스의 체에 따라 limit 까지만 배수 여부를 확인한다
    for i in range(2, lim+1):
        if num % i == 0: # 'num' 이 'i' 의 배수라면,
            return False
    
    return True # 지금 숫자는 소수이다.

def solution(numbers):
    count = 0 # 주어진 문자열의 총 소수 개수
    
    # 1. 모든 숫자 조합 만들기
    recur("", numbers)
    
    # 2. 소수 판별
    for it in numberSet: # 지금까지 조합한 모든 숫자를 하나씩 꺼내서 확인한다
        if isPrime(it): # 소수일 때,
            count += 1
    
    return count
