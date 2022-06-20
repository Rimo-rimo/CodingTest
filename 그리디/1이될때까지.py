data, k = map(int, input().split())
cnt = 0
while data != 1 and data >= k:
    if data % k == 0:
        cnt += 1
        data = data//k
    else:
        cnt += (data % k)
        data -= (data % k)
if data != 1:
    cnt += (data-1)
print(cnt)
