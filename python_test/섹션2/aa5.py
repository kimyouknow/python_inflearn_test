import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())

cnt = [0]*(n+k+3)
print(cnt)
max=0
for i in range(1, n + 1):
    for j in range(1, k + 1):
        cnt[i+j] += 1
print(cnt)

for i in range(n+k+1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n+k+1):
    if cnt[i] == max:
        print(i, end=' ')

# n, m = map(int, input().split())

# cnt = 0
# List = [0] * (n + m)

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         sum = i + j
#         for k in range(len(List)):
#             if k == sum - 1:
#                 List[k] += 1

# max = 0
# for i in range(n+m):
#     if List[i] > max:
#         max = List[i]

# for i in range(n + m):
#     if List[i] == max:
#         print(i+1, end=" ")


     
          
      