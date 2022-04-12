# 최대공약수와 최소공배수

# =====첫번째 풀이=====
# A,B = map(int,input().split())
# a,b = A,B

# # 최대 공약수
# l = 1
# for i in range(2, min(a,b)+1):
#     if A%i == 0 and B%i==0:
#         l=i
# print(l)

# # 최소 공배수

# while True:
#     if A == B:
#         print(A)
#         break
#     elif A < B:
#         A += a
#     else:
#         B += b

# =====개선된 풀이=====
# 유클리드 호제법
a,b = map(int,input().split())

def gcd(x,y):
    if x%y == 0:
        return y
    else:
        return gcd(y, x%y)

l = gcd(a,b)
s = a*b//l
print(l)
print(s)