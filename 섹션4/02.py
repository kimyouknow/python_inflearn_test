import sys
sys.stdin = open("input.txt", "rt")
k, n = map(int, input().split())

def count(mid):
    cnt = 0
    for x in temp:
        cnt += (x//mid)
    return cnt

temp = []
big = 0
for x in range(k):
    x = int(input())
    temp.append(x)
    big = max(x, big)

lt = 1
rt = big
res = 0
while lt <= rt:
    mid = (rt+lt)//2
    if count(mid) < n:
        rt = mid - 1
    else:
        res = mid
        lt = mid + 1
print(res)

# 답; 랜선의 최대 길이 > 랜선의 최소 = 1, 최대 = 802
# mid = 401 > 만들수 있는 랜선의 길이 n = 2, 1, 1, 1 => 5개 
# 이러면 n을 늘려야하니가  mid를 줄여야함 ; rt = mid = 401
# mid = 200 > n = 4,3, 2, 2 > 11개
# 더 좋은 숫자가 있나 확인해야함 ; lt = mid = 200
# mid = 300 > n = 2,2,1,1 > 6개 

# 만약 mid가 200보다 작을땐? n 11개보다 클때
# lt =mid로 범위를 줄여아함