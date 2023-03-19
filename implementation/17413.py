# 단어 뒤집기 2 백준 17413번

# 의사코드
# 괄호 사이의 문자열은 뒤집으면 안되기 때문에 "<" 를 만나면 ">" 를 만날 때 까지는 그대로 둔다.

# 알파벳이나 숫자일 경우, 뒤집어야 하기 때문에

# 단어를 구분짓는 공백이나, 혹은 괄호를 만나기 전까지 뒤집어준다.

# 또한, 띄어쓰기를 만나게 되면 그냥 i +=1 을 통해 지나간다.


import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 열린 괄호를 만나면
        i += 1 
        while word[i] != ">":      # 닫힌 괄호를 만날 때 까지
            i += 1 
        i += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        print('before start: ',start,' before i: ',i)
        while i < len(word) and word[i].isalnum():
            i+=1        
        tmp = word[start:i] # 숫자,알파벳 범위에 있는 것들을
        print('tmp: ',tmp)
        print('word[start:i]: ',word[start:i])
        print('start: ',start,' i: ',i)
        tmp.reverse()       # 뒤집는다
        word[start:i] = tmp
    else:                   # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i+=1                # 그냥 증가시킨다

print("".join(word))
print(word)
