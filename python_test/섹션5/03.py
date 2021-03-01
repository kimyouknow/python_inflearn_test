# 연산자면 다음 숫자뒤로 넘기기
# stack = [] 3  5 + 

import sys
sys.stdin = open("input.txt", "r")
n = input()
# 내풀이; stack에 정답을 쌓는 방식, temp라는 기호를 담는 리스트를 만들어서
# 여러 조건의 if문으로 풀었음, try문으로 연산자랑 숫자를 구분해서 풀었음

# 해설; stack에 연산자를 담음 => 내풀이와 차이점- 연산자의 우선순위를 고려해서 
# stack에 쌓음. stack에 처음 담긴애가 제일 늦게 실행되는 애들
# stack의미 연산자를 만나면, 만난 연산자보다 우선순위가 높거나 같은 애들만 출력 


stack = []
res = ''
for x in n:
    if x.isdecimal():
        res += x
    else:
        if x == "(" :
            stack.append(x)
        elif x == "*" or x =="/":
            while stack and (stack[-1] == '*' or stack[-1] == "/"):
                res += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ")":
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop() # ( 이걸 없애버려야함. 출력을 안하고 
# for문 처리 후 stack에 남아 있는 연산자 처리
while stack:
    res += stack.pop()

print(res)