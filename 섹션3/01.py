import sys
sys.stdin = open("input.txt", "rt")
n = int(input())

# cnt = 0
# for x in range(n):
#     x = input().lower()
#     cnt += 1
#     if x == x[::-1]:
#         print("#%d YES" %(cnt))
#     else:
#         print("#%d NO" %(cnt))

for i in range(n):
    s = input().lower()
    size = len(s)
    for j in range(size // 2):
        if s[j] != s[-1-j]:
            print("#%d No" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

    


