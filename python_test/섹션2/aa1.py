import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())

cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else: 
    print(-1)

# n = int(n)
# m = int(m)
# res = []
# for i in range(1, n+1):
#     if n % i == 0:
#         res.append(i)

# print(res)
# if len(res) < m:
#     print(-1)
# else:
#     print(res[m-1])