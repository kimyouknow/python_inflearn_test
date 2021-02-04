import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
# 키 기준으로 정렬한 다음, 몸무게 기준으로 다시 정렬
# 이중 포문으로 제거

player = []
for _ in range(n):
    cm, kg = map(int, input().split())
    player.append((cm, kg))
player.sort(reverse=True)
largest = 0
cnt = 0
for cm, kg in player:
    if kg > largest:
        largest = kg
        cnt += 1
print(cnt)


# player.sort()

# temp_cm = 0
# temp_kg = 0
# cnt = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         if player[i][1] < player[j][1]:
#             cnt += 1
#             break
# print(n-cnt)



