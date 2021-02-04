import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

# for i in range(m):
#     h, t, k = map(int, input().split())
#     if t == 0:
#         for _ in range(k): # 아래 두 줄을 k번 반복 > 동영상강의는 range(k)라고함 
#             x = a[h-1].pop(0) # 특정 부분 pop하면 뒤에 부분은 땡겨짐
#             a[h-1].append(x) # 이걸 다시 땡겨진 리스트 맨 뒤로 붙힘
#     else:
#         for _ in range(k):
#             x = a[h-1].pop()
#             a[h-1].insert(0, x) 

# res = 0
# s = 0
# e = n-1
# for i in range(n):
#     for j in range(s, e+1):
#         res += a[i][j]
#     if i < n//2:
#         s += 1
#         e -= 1
#     else:
#         s -= 1
#         e += 1
# print(res)

b = [list(map(int, input().split())) for _ in range(m)]
temp = []
# b의 첫번째 수에 해당하는 a의 행 뽑기
for i in range(n):
    for j in range(m):
        if i == b[j][0]-1:
            # 왼쪽 오른쪽 돌리기 못했었음 
            # if b[j][1] == 0: # 왼
            #     for _ in range(b[j][2]):
            #         x = a[i].pop(0)    
            #         a[i].append(x)
            # else: # 오
            #     for _ in range(b[j][2]):
            #         x = a[i].pop()    
            #         a[i].insert(0, x)
for x in a:
    print(x)

#모래시계
res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i >= n//2: # i > n//2: 이렇게 썼었음 
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)
        