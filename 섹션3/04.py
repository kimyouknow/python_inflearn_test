import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

c = []
p1 = 0
p2 = 0

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]

for x in c:
    print(x, end=' ')



# if n < m:
#     s_num = n
#     b_num = m
#     s_list = a
#     b_list = b
# else:
#     s_num = m
#     b_num = n
#     s_list = b
#     b_list = a


# while p1 < s_num:
#     if s_list[p1] <= b_list[p2]:
#         c.append(s_list[p1])
#         p1 += 1
#     else:
#         c.append(b_list[p2])
#         p2 += 1

# c = c + b_list[p2:b_num]
# print(c)



# for i in range(m):
#     a.append(b[i])
#     a.sort()

# print(a)

