import sys
sys.stdin = open("input.txt", "rt")
n = int(input())

res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    # print( a, b, c)
    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = c * 100
    
    if money > res:
        res = money
print(res)


# num_list = [0] * n
# res = []
# for i in range(n):
#     num_list[i] = list(map(int, input().split()))
#     dice = num_list[i]

#     # print(num_list[i])
#     if dice[0] == dice[1] and dice[0] == dice[2]:
#         all_same = 10000 + dice[0] * 1000
#         res.append(all_same)
#     elif dice[0] != dice[1] and dice[0] != dice[2]: 
#         all_dif = max(dice) * 100
#         res.append(all_dif)
#     else:
#         if dice[0] == dice[1]:
#             one_dif = dice[0] * 100 + 1000
#             res.append(one_dif)
#         elif dice[0] == dice[2]:
#             one_dif = dice[0] * 100 + 1000
#             res.append(one_dif)
#         else:
#             one_dif = dice[0] * 100 + 1000
#             res.append(one_dif)

# print(max(res))




            


