# 아래와 같이 재귀를 사용하게 되면 백준에 제출시 RecursionError 가 발생한다.
# 재귀의 깊이가 너무 깊어 백준 페이지에서는 채점이 불가능하다.
---
import sys
input_fn = sys.stdin.readline

def recur(dwarf: list):
    sum = 0
    # 2. 반복문을 돌며 각 리스트의 수를 합한다.
    for i in range(len(dwarf)):
        if i == 7: # 합한 인덱스가 7 일 때,
            if sum == 100: # 지금까지 합한 값이 100 일 때,
                return
            else: # 100 이 아닐 때,
                dwarf.append(dwarf[0]) # 첫번째 인덱스 값을 마지막 인덱스로 옮긴다
                dwarf.remove(dwarf[0]) # 첫번째 인덱스를 삭제한다.
                recur(dwarf) # 새로운 순서로 일곱난쟁이를 찾는다.
        sum += dwarf[i]


def solution(dwarf: list):
    real = []
    
    recur(dwarf)
    
    # 3. 반복문으로 7번까지 새로운 리스트에 저장한다.
    for i in range(7):
        real.append(dwarf[i])
    
    real.sort() # 4. 진짜 난쟁이를 정렬한다.

    for i in range(len(real)):        
        print(real[i]) # 5. 한 줄씩 난쟁이츨 출력한다.

dwarf = []
for i in range(9):
    dwarf.append(int(input_fn())) # 1. 일곱난쟁이를 리스트에 담는다.

solution(dwarf)

---
# 재귀를 사용하지 않고 풀이한 방법
import sys
input_fn = sys.stdin.readline

def solution(dwarf: list):
    totalHeight = sum(dwarf)
 
    finish = False
    for i in range(8):
        for j in range(i + 1, 9):
            if (dwarf[i] + dwarf[j] == totalHeight - 100):
                save = [i, j]
                finish = True
                break
 
        if (finish):
            break
 
    del dwarf[save[0]]
    del dwarf[save[1] - 1]
 
    dwarf.sort()
 
    for i in dwarf:
        print(i)


dwarf = []
for i in range(9):
    dwarf.append(int(input_fn())) # 1. 일곱난쟁이를 리스트에 담는다.

solution(dwarf)
