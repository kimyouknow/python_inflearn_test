import sys
sys.stdin = open("input.txt", "rt")

def count(capacity):
    cnt = 1
    sum = 0
    for x in temp:
        if sum+x > capacity: 
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

n, m = map(int, input().split())
temp = list(map(int, input().split()))

lt = max(temp)
rt = sum(temp)
res = 0
while lt < rt:
    mid=(lt+rt)//2
    if count(mid) <= m:
        res = mid
        rt = mid-1
    else:
        lt = mid+1
print(res)