# 골드바흐의 추측

# 에라토스테네스의 체
re = [False, False] + [True]*(1000000 - 1)
result = []
for i in range(2,1000000+1):
    if re[i]:
        for j in range(i*2, 1000000+1, i):
            re[j]=False
        if i != 2:
            result.append(i)

# 판정 알고리즘
while True:
    n = int(input())
    if n == 0:
        break
    for i in result:
        k = n - i
        if re[k]:
            print(f"{n} = {i} + {k}")
            break

    