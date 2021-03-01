import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
A = list(map(int, input().split()))

lt = 0
rt = 1
tot = A[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += A[rt]
            rt += 1
        else:   
            break
    elif tot == m:
            cnt += 1;
            tot -= A[lt]
            lt += 1
    else:
        tot -= A[lt]
        lt += 1
print(cnt)


# for i in range(n):
#     for j in range(i+1,n+1):
#         res = A[i:j]
#         # print(res)
#         r = sum(res)  
#         # print(r)     
#         if r == m:
#             cnt += 1
# print(cnt)



