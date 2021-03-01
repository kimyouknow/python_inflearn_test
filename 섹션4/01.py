import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n - 1 
# 12 23 32 57 65 81 87 99
# 0  1  2  3  4  5  6  7
# mid = 3       a[mid] = 57 > m 
while lt < rt:
    mid = (lt + rt)//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid
        print(rt)
    else:
        lt = mid
        print(lt)


    