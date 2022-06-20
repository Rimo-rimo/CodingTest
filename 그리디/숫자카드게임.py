n,m = map(int,input().split()) # n:행, m:열
data = []
for i in range(n):
    data.append(min(list(map(int,input().split()))))
print(max(data))
