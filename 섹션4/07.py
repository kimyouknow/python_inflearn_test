import sys
sys.stdin = open("input.txt", "rt")
l = int(input())
boxes = list(map(int, input().split()))
m = int(input())
# m = 3

# for문을 돌때마다
# 오르차순 정렬 > 맨뒤 -1, 맨앞 +1
for _ in range(m):
    boxes.sort()
    boxes[0] = boxes[0]+1
    boxes[l-1] = boxes[l-1]-1
    
boxes.sort()
sub = boxes[l-1] - boxes[0]
print(sub)