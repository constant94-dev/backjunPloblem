def solution(a, b, n):
    coke = 0
    
    while n >= a:
        newCount = n//a * b
        coke += newCount
        n = n % a + newCount
    return coke
