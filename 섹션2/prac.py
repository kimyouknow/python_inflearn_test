import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
l = list(map(int, input().split()))

sum = 0
cnt = 0
for i in range(n):
    if l[i] == 1:
        for j in range(i-1, 0):
            cnt += 1
            if l[j] == 0:
                break
            sum += cnt
print(sum)
            
        