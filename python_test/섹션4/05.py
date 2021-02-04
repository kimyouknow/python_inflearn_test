import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
# 어떻게 이을까?
# 끝나는 시간 기준으로 정렬 
# for문으로 한 줄씩 돌면서, 해당 줄의 꼬리 숫자가 다음 줄에 머리 숫자보다 
# 작으면 cnt += 1
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort(key=lambda x: (x[1], x[0]))
et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1
print(cnt)



# temp = []
# for _ in range(n):
#     tmp = list(map(int, input().split()))
#     tmp.reverse()
#     temp.append(tmp)
# temp.sort()

# st = 0
# et = 0
# cnt = 0
# for i in range(n):
#     if et <= temp[i][1]:
#         cnt += 1
#         et = temp[i][0]
#         st = temp[i][1]
#         print(i)
# print(cnt)