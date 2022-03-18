import sys

num = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
result = [-1]*num
stack = [0]

for i in range(1,num):
    while True:
        if stack and a[stack[-1]] < a[i]:
            result[stack.pop()] = a[i]
        else:
            break
    stack.append(i)

print(*result)
