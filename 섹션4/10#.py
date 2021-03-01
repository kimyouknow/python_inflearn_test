import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
# 역수열이 주어짐
# 큰 숫자일수록 자유도가 높음
# 작은 숫자일수록 위치가 정해짐 => 작은 숫자부터 채우기
res = [0] * n
# print(a)
# 5 3 4 0 2 1 1 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 1 0 0 
# 0 0 0 2 0 1 0 0 
# 0 0 0 2 0 1 3 0 
# 4 0 0 2 0 1 3 0 
# 4 0 0 2 5 1 3 0
# 0의 개수를 세어야 함 

cnt = 0
num = 1 # 답에 들어갈 숫자
while a: 
    m = a[0]
    for i in range(n):
        if res[i] == 0:
            cnt += 1
        if cnt == m+1:
            res[i] = num
            num += 1
            break
    a.pop(0)
    cnt = 0
# print(res)
for x in res:
    print(x, end=' ')


# 해설
for i in range(n):
    for j in range(n):
        if a[i] == 0 and res[j] == 0: #a[i] == 0 => 자기 앞에 빈공간을 확보했다 // res[j] == 0 => res가 0이 아닐땐 하나 더 뒤로 가라
            res[j] = i+1
            break
        elif res[j] == 0: #a[i] != 0 
            a[i] -= 1
for x in res:
    print(x, end=' ')            
# i = 0일때, a[0] = 5 > 4> 3> 2> 1> 0 ==> a[i]가 0이 될때까지 j는 증가, 따라서 이때 j = 5
# res[5] = 0 + 1