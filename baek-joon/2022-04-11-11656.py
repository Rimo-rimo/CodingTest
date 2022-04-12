# sort는 문자열을 사전순으로도 정렬해준다.
a = input()
result = []
for i in range(len(a)):
    result.append(a[i:])
for i in sorted(result):
    print(i)