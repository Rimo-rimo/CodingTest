import sys
input=sys.stdin.readline

num = int(input())
stack = []
for i in range(num):
    comm = input().split()
    if len(comm) == 2:
        stack.append(comm[-1])
    else:
        result = int()
        if len(stack) == 0:
            result = -1
        elif comm == ["pop"]:
            result = stack.pop()
        elif comm == ["top"]:
            result = stack[-1]
        if comm == ["size"]:
            result = len(stack)
        if comm == ["empty"]:
            if result == -1:
                result = 1
            else:
                result = 0
        print(result)