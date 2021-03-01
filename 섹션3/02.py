import sys
sys.stdin = open("input.txt", "rt")

s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)

# n = input()
# cnt = 0
# x = 0
# for i in n:
#     try:
#         x = int(i) + x * 10
#     except ValueError:
#         pass

# for i in range(1, x+1):
#     if x % i == 0:
#         cnt += 1

# print(x)
# print(cnt)

