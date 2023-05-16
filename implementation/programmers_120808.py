def gcd(a: int, b: int):
    if a % b == 0:
        return b
    return gcd(b, a%b)

def solution(numer1, denom1, numer2, denom2):
    # 두 분수의 합 계산
    boonja = numer1 * denom2 + numer2 * denom1 # 기약분수를 고려하지 않는 분자
    boonmo = denom1 * denom2 # 기약분수를 고려하지 않는 분모
    
    # 최대공약수 계산
    gcd_value = gcd(boonmo, boonja)
    
    # gcd 로 나눈 값을 answer 에 담기
    answer = [boonja // gcd_value, boonmo // gcd_value]
    return answer
