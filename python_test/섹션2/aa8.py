import sys
sys.stdin = open("input.txt", "rt")
n = input()
a = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x//10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2 + 1):
        if x%i == 0:
            return False
    else:
        return True 


for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')


# def reverse(x):
#     reverse_list = []
#     for i in range(int(n)):
#         variable = str(a[i])
#         if variable[len(variable)-1] == '0':
#             while variable[len(variable)-1] == '0':
#                 variable = variable[:len(variable)-1]
#             reverse_list.append(variable[::-1])
            
                      
#         else:
#             reverse_list.append(variable[::-1])
#     return(reverse_list)

# def isPrime(x):
#     y = len(x)
#     for k in range(y):
#         z = int(x[k])
#         ch = [0] * (z+1)
#         list = []
#         for i in range(2, z+1):
#             if ch[i] == 0:
#                 list.append(i)
#                 for j in range(i, z+1, i):
#                     ch[j] = 1
#         last = len(list)-1
#         if list[last] == z:
#             print(z)
        

# def init():
#     number = reverse(a)
#     isPrime(number)
    


# init()


