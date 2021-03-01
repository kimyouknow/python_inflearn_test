import sys
sys.stdin = open("input.txt", "rt")
a = [list(map(int, input().split())) for _ in range(7)]
n = 3
cnt = 0
for i in range(7):
    for k in range(n):
        if a[i][k] == a[i][4+k] and a[i][1+k] == a[i][3+k]:
            cnt += 1
        if a[k][i] == a[4+k][i] and a[k+1][i] == a[k+3][i]:
            cnt += 1
print(cnt)



