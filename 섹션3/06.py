import sys
sys.stdin = open("input.txt", "rt")
n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

largest = 0
for i in range(n):
    sum1 = sum2 = 0
    # s1; 행, s2; 열
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
    if sum2 > largest:
        largest = sum2

print(largest)






# for x in a:
#     print(x)
cul_sum = 0
row_sum = 0
cul_max = 0
row_max = 0

for i in range(n):
    for j in range(n):
        row_sum += a[i][j]
    if row_sum > row_max:
        row_max = row_sum
    row_sum = 0
# print(row_max)

for i in range(n):
    for j in range(n):
        cul_sum += a[j][i]
    if cul_sum > cul_max:
        cul_max = cul_sum
    cul_sum = 0
# print(cul_max)

dia_sum1 = 0
dia_sum2 = 0
# 00 11 22 33 44 
# 04 13 22 31 40
for i in range(n):
    dia_sum1 += a[i][i]
    dia_sum2 += a[i][n-i-1]
# print(dia_sum2, dia_sum1)
ans = [row_max, cul_max, dia_sum2, dia_sum1]
max = 0
for x in ans:
    if x > max:
        max = x
print(max)

