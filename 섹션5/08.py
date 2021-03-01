import sys
sys.stdin = open("input.txt", "r")
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1):
    word = input()
    p[word] = 0
for key, val in p.items():
    if val == 1:
        print(key)
        break


# written = []
# for i in range(2 * n - 1):
#     word = input()
#     if i < n:
#         written.append(word)
#     else:
#         if word in written:
#             written.pop(written.index(word))
# print(written)
