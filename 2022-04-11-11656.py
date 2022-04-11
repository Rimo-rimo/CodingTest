a = input()
result = []
for i in range(len(a)):
    result.append(a[i:])
for i in sorted(result):
    print(i)