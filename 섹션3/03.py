import sys
sys.stdin = open("input.txt", "rt")

a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1//2)):
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0)
for x in a:
    print(x, end=' ')

# li1 = [0] * 20
# li2 = [0] * 20
# for x in range(1, 21):
#     li1[x-1] = x
#     li2[x-1] = x

# n = 2
# for _ in range(n):
# s, e = map(int, input().split())
# print(s, e)
# 실패
# for i in range(e-s+1):    
#     li2[s-1+i] = li1[e-1-i]
# li1 = li2
# print(li2)

#성공
#     temp = li1[s-1:e]
#     temp = li1[:s-1] + list(reversed(temp)) + li1[e:]
#     li1 = temp
#     print(temp)
    

