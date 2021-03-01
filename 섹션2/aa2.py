import sys
sys.stdin = open("input.txt", "rt")
T = int(input())
for t in range(T):
    n, s, e, k= map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))


res = []
# for i in range(int(t)):
#     n, s, e, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     for j in range(s-1, e):
#         res.append(a[j])
#     res.sort()
#     print("#%d %d" %(i+1, res[k-1]))
#     res = []

