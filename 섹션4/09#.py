import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
m = list(map(int, input().split()))
lt = 0 
rt = n-1
last = 0
res=""
temp = []
while lt <= rt:
    if m[lt] > last:
        temp.append((m[lt], 'L'))
    if m[rt] > last:
        temp.append((m[rt], 'R'))
# 여기까지 둘다 들어왔다면 둘 중에 작은 값을 선택해야함 
    temp.sort() # 그래서 정렬해서 temp내에서 정렬됨 
    if len(temp) == 0:
        break
# temp에 아무것도 못넣었다는것은 lt, rt 둘다 last보다 작다는 뜻 
    else:
        # len(temp) != 0이면 한개아니면 두개가 temp에 들어간것 
        res = res+temp[0][1] # 문자열은 어차피 그냥 뒤에가서 붙음  
        last = temp[0][0]
        if temp[0][1]=='L':
            lt += 1
        else:
            rt -= 1
    temp.clear()
print(len(res))
print(res)