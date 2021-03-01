import sys
sys.stdin = open("input.txt", "r")
n = list(input())
# for문으로 주어진 문자열을 돌면서 연산자를 만나면 앞에 두 자리 더하기 
# 더한 값을 ()안에 넣기 
# 언제까지? for문이 끝까지 돌 때까지

stack = []
for x in n:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=="+":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2+n1)
        elif x=="-":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
        elif x=="*":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2*n1)
        elif x=="/":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2/n1)
print(stack[0])




# while len(n) > 1:
#     for i in range(len(n)):
#         if n[i].isdecimal():
#             pass
#         else: # 연산자
#             if n[i] == "+":
#                 temp = int(n[i-1]) + int(n[i-2])
#                 n.pop(i)
#                 n.insert(i, str(temp))
#                 n.pop(i-1)
#                 n.pop(i-2)
#             elif n[i] == "-":
#                 temp = int(n[i-2]) - int(n[i-1])
#                 n.pop(i)
#                 n.insert(i, str(temp))
#                 n.pop(i-1)
#                 n.pop(i-2)
#             elif n[i] == "*":
#                 temp = int(n[i-1]) * int(n[i-2])
#                 n.pop(i)
#                 n.insert(i, str(temp))
#                 n.pop(i-1)
#                 n.pop(i-2)
#             elif n[i] == "/":
#                 temp = int(n[i-2]) / int(n[i-1])
#                 n.pop(i)
#                 n.insert(i, str(temp))
#                 n.pop(i-1)
#                 n.pop(i-2)
#             break 
# print(n[0])
