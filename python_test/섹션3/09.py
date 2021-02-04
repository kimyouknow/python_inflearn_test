import sys
sys.stdin = open("input.txt", 'rt')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
zero = []
for i in range(n):
    a[i].insert(0, 0)
    a[i].insert(n+1, 0)

for i in range(n+2):
       zero.append(0)

a.insert(n+1, zero)
a.insert(0,zero)
cnt = 0
# 시계방향 탐색
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n+2):
    for j in range(n+2):
        if all((a[i][j] > a[i+dx[k]][j+dy[k]]) for k in range((4))):
            cnt += 1



# for i in range(n+2):
#     for j in range(n+2):
#         if a[i][j] != 0:
#             if a[i][j] > a[i-1][j] and a[i][j] > a[i+1][j] and a[i][j] > a[i][j-1] and a[i][j] > a[i][j+1]:
#                 cnt += 1
print(cnt)
# 상 a[i][j] > a[i-1][j]
# 하 a[i][j] > a[i+1][j]
# 좌 a[i][j] > a[i][j-1]
# 우 a[i][j] > a[i][j+1]

            