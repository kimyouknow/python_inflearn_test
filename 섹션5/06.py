# 접수한 순대대로 제일 앞에 환자 꺼내기
# 나머지 대기목록에서       지금 꺼낸 환잗보다 높은 위험도가 존재하면
# 방금 꺼냔 환자를 맨 뒤로
# 5 2
# 60 50 70 80 90
# 60 50 70
# => 90 70
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0  # 진료받는 번째
while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break
print(cnt)

# n, m = map(int, input().split())
# application = list(map(int, input().split()))
# deque = list()
# deque = dq(deque)

# for index, x in enumerate(application):
#     temp = [index, x]
#     deque.append(temp)

# # 하나씩 들어와서 뒤에 전체 중 max보다 작으면 뒤로
# # 같거나 크면 그대로 pop
# # max를 구하는 방법;
# res = []
# cnt = 0
# while deque:
#     temp_max = max(deque, key=lambda item: item[1])
#     if deque[0][1] < temp_max[1]:
#         deque_popleft = deque.popleft()
#         deque.append(deque_popleft)
#     else:
#         ans = deque.popleft()
#         cnt += 1
#         if ans[0] == m:
#             print(cnt)
#             break
