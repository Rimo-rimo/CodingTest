# 소수찾기
# ======첫번째 풀이======
n = int(input())
a = list(map(int,input().split()))
count = 0
for i in a:
    if i == 1:
        count += 1
        continue
    if i != 2:
        for k in range(2,i//2 + 1):
            if i%k == 0:
                count += 1
                break
print(n - count)


