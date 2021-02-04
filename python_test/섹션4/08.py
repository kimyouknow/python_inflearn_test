import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
passenger = list(map(int, input().split()))
passenger = deque(passenger)

passenger.sort()
cnt = 0
while passenger:
    if len(passenger) == 1:
        cnt += 1
        break
    if passenger[0] + passenger[-1] > m:
        passenger.pop()
        cnt += 1
    else:
        passenger.popleft()
        # passenger.pop(0)
        passenger.pop()
        cnt += 1
print(cnt)

# list자료는 앞에꺼 pop시키면 뒤에 애들이 차례대로 채워지는 비효율적인 연산을 함 


