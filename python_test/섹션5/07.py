import sys
sys.stdin = open("input.txt")
from collections import deque

need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft(): # 순서가 다름
                print("#%d No" %(i+1))
                break;
    else: #순서는 통과
        if len(dq) == 0: # 제대로 짠거
            print("#%d YES" %(i+1))
        else:
            print("#%d No" %(i+1))




# ess = input()
# n = int(input())
# temp = []
# res = []
# for i in range(n):
#     course = input()
#     for x in course:
#         for y in ess:
#             if x == y:
#                 res.append(x)
#     if res == list(ess):
#         print(i+1, 'YES')
#     else:
#         print(i+1, "NO")
#     res = []


# ess와 course를 동시에 index-0부터 비교해서 
# index-0이 같으면 ess와 course에서 둘다 빼고
# index-0이 다르면 course만 뒤로 
# ess가 []면 yes, 남아있으면 no
# 이러면 순서가 상관없어서 답이 안나옴
# 순서를 지켜야함 