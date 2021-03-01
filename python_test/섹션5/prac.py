import sys
sys.stdin = open("input.txt", "r")
a = input()
b = input()
dic = dict()

str1 = [0]*52
str2 = [0]*52

for x in a:
    if x.isupper():
        str1[ord(x)-65] += 1
    else:
        str1[ord(x)-71] += 1
print(str1)
