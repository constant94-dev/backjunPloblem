# 숫자 카드 나누기

# 재귀를 활용한 최대공약수 구하기
def gcd(a, b):
    if a % b == 0: return b
    return gcd(b, a%b)

# 서로의 최대공약수로 철수 or 영희의 카드들을 하나씩 나눠본다.
def notDivisible(arr: list, num: int):
    for x in arr:
        if x % num == 0:
            return False
    return True

def solution(arrayA, arrayB):
    # 철수의 최대공약수 or 영희의 최대공약수가 배열의 첫번째 인덱스의 값이라고 가정한다.
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    answer = 0
    # 철수가 가진 카드들의 최대공약수, 영희가 가진 카드들의 최대공약수를 구한다.
    for i in range(1, len(arrayA)):
        gcdA = gcd(gcdA, arrayA[i])
        gcdB = gcd(gcdB, arrayB[i])
    
    # 철수가 가진 카드들의 최대공약수로 영희가 가진 카드들을 하나씩 나눠본다.
    # 나눠지면, answer = 0
    # 안나눠지면, answer = 철수가 가진 카드들의 최대공약수를 대입
    if notDivisible(arrayB, gcdA):
        if answer < gcdA:
            answer = gcdA

    # 영희가 가진 카드들의 최대공약수로 철수가 가진 카드들을 하나씩 나눠본다.
    # 나눠지면, answer = 0
    # 안나눠지면, answer = 영희가 가진 카드들의 최대공약수를 대입
    if notDivisible(arrayA, gcdB):
        if answer < gcdB:
            answer = gcdB
    # 최댓값 반환
    return answer
