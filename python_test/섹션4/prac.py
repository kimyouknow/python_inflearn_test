import sys
sys.stdin = open("input.txt", "rt")
k = int(input())
rev = list(map(int, input().split()))
ans = [0] * k
print(k ,rev, ans)
# 5 3 4 0 2 1 1 0
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 1 0 0
# 0 0 0 2 0 1 0 0 
# 0 0 0 2 0 1 3 0 
# 4 0 0 2 0 1 3 0
# 자기 자리 rev 숫자 + 1에 원래 숫자를 넣어야함
for i in range(k):
    for j in range(k):
        