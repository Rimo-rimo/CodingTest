# 소수구하기
# 에라토스테네스의 체

s,m = map(int,input().split())

result = [False, False] + [True]*(m-1)

for i in range(2,m+1):
    if result[i]:
        for j in range(i*2,m+1,i):
            result[j] = False
        if i >= s:
            print(i)
    

