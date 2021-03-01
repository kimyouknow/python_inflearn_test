import sys
sys.stdin = open("input.txt", "rt")
a, m = map(str, input().split())

# 앞에서부터 차례대로 진행되면서
# 앞에 숫자가 뒤에 숫자보다 크면 통과 
# 앞에 숫자가 뒤에숫자보다 작으면 앞에숫자제거 > 
# 제거할때, 앞 모든 숫자의 max로 판단
# tmax = 0이라는 변수로 앞의 모든 숫자의 max
# mp = 0으로 tmax와 상관없이 하나씩 증가 
# while m > 0일때를 기준으로 생각함

# 스택; 자리이 용이한 자료구조. 
# lifo; last in first out
# 들어가는 입구와 나오는 출구가 한 곳인 공간 => 나중에 들어간게 먼저나와야함
# list를 예로들면, pop(), append()를 이용하면 구현 가능

# 하나씩 지우면 됬는데 한 번에 모두 지울려고 생각하니까 구현이 안됬음
# 스택구조로 생각해서 맨뒤에 껄로 비교해야하는데 계속 앞에서부터 비교했음 
ans = [0]
temp = 0
m = int(m)
for i in range(len(a)):
    x = int(a[i])
    last = ans[len(ans)-1]
    if x > last: 
        while m > 0 and len(ans) > 1:
            if x <= last:
                break
            else:
                ans.pop()
                m -= 1
        ans.append(x)
    else: # x < last
        ans.append(x)
if m > 0:
    print(ans[1:-m])
else:
    print(ans[1:])
