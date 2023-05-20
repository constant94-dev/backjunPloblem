def notDivisible(arr: list, num: int):
    for n in arr: # arr 배열의 모든 요소를 확인한다
        if n % num == 0:
            return False # 이 함수는 나눠지면 안되는걸 검증하는 함수이니 나누어질 때는 false 반환
    return True

def gcd(a: int, b: int):
    while b != 0:
       a, b = b, a%b
    return a # 마지막으로 계산된 a 가 최대공약수
    # if a % b == 0:
    #     return b
    # return gcd(b, a%b) # 이전의 사용한 방법

def solution(arrayA, arrayB):
    result = 0 # 가장 큰 양의 정수
    gcdA = arrayA[0] # 각 배열의 첫번째 값이 최대공약수라고 가정한다
    gcdB = arrayB[0]
    
    # 1. 각 배열의 최대공약수 구하기
    for i in range(1, len(arrayA)): # 변수로 '0'번 인덱스는 사용했으니 1번부터 시작한다
        gcdA = gcd(gcdA, arrayA[i])
        gcdB = gcd(gcdB, arrayB[i])
    
    # 2. 서로의 배열을 나눌 수 없는지 확인하기
    # arrayA 의 최대공약수를 가지고 arrayB 배열이 나눠지지 않는지
    # arrayB 의 최대공약수를 가지고 arrayA 배열이 나눠지지 않는지 확인한다
    if notDivisible(arrayB, gcdA):
        if result < gcdA: # 현재 결과값이 arrayA 배열의 최대공약수 값보다 작은가
            result = gcdA
    
    if notDivisible(arrayA, gcdB):
        if result < gcdB: # 현재 결과값이 arrayB 배열의 최대공약수 값보다 작은가
            result = gcdB

    # 3. 최대값 반환
    return result
