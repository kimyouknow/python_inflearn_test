# n명의 학생 수학 점수
# n명의 학생들의 평균(소수 첫째자리 반올림)
# n명의 학생중 평균에 가장 가까운 학생은 몇 번째인지
#  
# 
#

import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))

avg = (sum(a) / n)
avg = avg + 0.5
avg = int(avg)
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x - avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
            
print(avg, res)

# n = int(input())
# l = list(map(int, input().split()))
# avg = int(sum(l) / n + 0.5)

# min = 2147000

# for idx, x in enumerate(l):
#     res = (avg - l[idx])
#     if res < 0:
#         res = abs(res)
#         if res < min:
#             min = res
#             ans = idx + 1


# print(avg, ans)
