# ()(((()())(())()))(())
# 0    0 0   0  0    0

# 하나씩 입력되면서 () 한 쌍이면 레이저
import sys
sys.stdin = open("input.txt", "rt")
n = input()

res = []
sum = 0
for i in range(len(n)):
    if n[i] == "(":
        res.append(n[i])
    else: # x==")"
        if n[i-1] == "(":
            res.pop()
            sum += len(res)   
        elif n[i-1] == ")":
            res.pop()
            sum += 1
            
print(sum)

# res = []
# sum = 0
# for x in n:
#     if x == "(":
#         res.append(x)
#     else: # x==")"\
#         if res[-1] == "(":
#             res.pop()
#             sum += len(res)   
#         elif res[-1] == ")":
#             res.pop()
#             sum += 1
            
# print(sum)

# 하나씩 들어오면서 괄호를 판단 
# res = [0]
# cnt = 0
# bui = 0
# for x in n:
#     if x == '(':
#         cnt += 1
#     else: # x == ')'
        
#     if x == '(' and res[-1] == ')':
#         bui += 1
#         cnt -= 1
#     elif x == ')' and res[-1] == '(':
    


#     res.append(x)
    
    # 내가 못한 부분; 스택처럼 생각하긴 했는데 더해야할 부분을 다르게 생각함
    # 내가 한 풀이 방식;
    # -개수 세는 변수를 따로 만듦,
    # - res = [0]으로 만들고 시작해서 뒤에 들어온 애를 기준으로 생각함 => 문풀은 앞에꺼 기준으로 생각함
    # - 스택의 구조를 활용하지 못함; append, pop
    # - res[-1]이 아니라 원래 수열자체에서 num[i-1]로 확인해야함 => res[-1]은 바귐