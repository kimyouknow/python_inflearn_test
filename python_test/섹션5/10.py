import sys
import heapq as hq
sys.stdin = open("input.txt")
a = []
while True:
    n = int(input())

    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)


# x = 2.9
# y = 0
# res = []
# ans = []
# while x >= 0:
#     x = int(input())
#     if x == -1:
#         break
#     res.append(x)
#     if x == 0:
#         res.pop()
#         res = sorted(res)
#         y = res.pop(0)
#         ans.append(y)

# for x in ans:
#     print(x)
