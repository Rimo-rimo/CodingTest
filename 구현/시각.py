N = int(input())
re = []
cnt = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            re = str(h)+str(m)+str(s)
            if "3" in re:
                cnt += 1
print(cnt)

