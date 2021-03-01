import sys
sys.stdin = open("input.txt", "rt")
n = input()
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x%10
        x = x//10
    return sum
max = -1
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)

# n = int(input())
# l = list(map(int, input().split()))
# def digit_sum(x):
#     sum = 0
#     while x > 0:
#         sum += x % 10
#         x = x // 10
#     return sum


# max = 0
# for num in l:
#     if digit_sum(num) > max:
#         max = digit_sum(num)
#         res = num
# print(res)
    

# def digit_sum(x):
#     add = 0
#     new = str(x)
#     for i in range(len(new)):
#         add += int(new[i])
#     return add

# max = 0
# for j in range(int(n)):
#     if digit_sum(a[j]) > max:
#         max = digit_sum(a[j])
#         ans = a[j]

# print(ans)
