import sys
sys.stdin = open("input.txt", "rt")
n = input()
n = int(n)

ch = [0] * (n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        print(i)
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)

# n = int(input())
# List = [0] * (n+1)
# cnt = 0

# for i in range(2, n+1):
#     if List[i] == 0:
#         cnt += 1
#         for j in range(i, n+1, i):
#             List[j] += 1
# print(cnt)



# res = list()
# for i in range(1, n+1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#         else:
#             res.append(i)
            
# res = set(res)
# print(res)    
# print(len(res)+1)
