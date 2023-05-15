import sys
input = sys.stdin.readline

def solution(num: list):
    for i in range(1, 31):
        num.append(i)

    for _ in range(28):
        n = int(input())
        num.remove(n)

num = []
solution(num)
print(min(num))
print(max(num))
