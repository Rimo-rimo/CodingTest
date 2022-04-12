# 최소공배수
n = int(input())

def gcd(x,y):
    if x%y == 0:
        return y
    else:
        return gcd(y,x%y)

for _ in range(n):
    a,b = map(int, input().split())
    print(a*b // gcd(a,b))