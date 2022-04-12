import sys
from collections import Counter

num = int(input())
n = list(map(int,sys.stdin.readline().split()))
counter = Counter(n)
re = [-1]*num
stack = [0]

for i in range(1,num):
    while stack and counter[n[i]] > counter[n[stack[-1]]]:
        re[stack.pop()] = n[i]
    stack.append(i)
print(*re)
