import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
print(n ,a)

sum = 0
cnt = 0
for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum, cnt)


# cnt = 0
# plus = 0
# a.insert(0, 0)
# for i in range(n+1):
#     if a[i] == 1:
#         while a[i] == 1:
#             plus += 1
#             cnt += plus
#             plus = 0
#             i -= 1
#     else:
#         cnt += 0
# print(cnt)
