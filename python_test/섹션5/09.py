# dict형태로 문자열1의 한글자씩 +=1 해서 받기

import sys
from collections import deque
sys.stdin = open("input.txt", "r")

a = input()
b = input()

# 아스키 풀이
str1 = [0]*52
str2 = [0]*52
for x in a:
    if x.isupper():
        str1[ord(x)-65] += 1
    else:
        str1[ord(x)-71] += 1
for x in b:
    if x.isupper():
        str2[ord(x)-65] += 1
    else:
        str2[ord(x)-71] += 1
# if str1 == str2: 이 방법도 됨
for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")


# st1 = dict()
# st2 = dict()

# sh = dict()
# for x in a:
#     sh[x] = sh.get(x, 0) + 1
# for x in b:
#     sh[x] = sh.get(x, 0) - 1
# for x in a:
#     if sh.get(x) > 0:
#         print("NO")
#         break
# else:
#     print("YES!")


# first = deque(input())
# second = list(input())
# while first:
#     for i in range(len(second)):
#         if first[0] == second[i]:
#             first.popleft()
#             second.pop(i)
#             break
#     else:
#         print("NO")
#         break
# if first == deque([]):
#     print("YES")
