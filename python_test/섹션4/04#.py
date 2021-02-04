import sys
sys.stdin = open("input.txt", "rt")

# 첫번째말은 제일 왼졲에 잇는 마구간에 놓는다고 가정,  

def count(mid):
    cnt = 1
    ep = temp[0] # 첫번쨰 마구간에 말 배치
    for i in range(1, n):
        if temp[i] - ep >= mid: 
            cnt += 1
            ep = temp[i]
    return cnt

n, c = map(int, input().split())
temp = []
for _ in range(n):
    x = int(input())
    temp.append(x)
temp.sort()
lt = 1
rt = temp[n-1]
while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)