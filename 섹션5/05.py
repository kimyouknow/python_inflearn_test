import sys
from collections import deque
sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)
while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft() # k번째 사람
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()




# res = []
# for i in range(n):
#     res.append(i+1)

# temp = []
# cur = 1
# while len(res) > 1:
#     i = 0
#     if cur == k:
#         res.pop(i)
#         cur = 1
#     else:
#         a = res.pop(i)
#         res.append(a)
#         cur += 1
# print(res[0])