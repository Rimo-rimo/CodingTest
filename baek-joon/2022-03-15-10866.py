from collections import deque
import sys

num = int(sys.stdin.readline())
dq = deque()

for i in range(num):

    c = sys.stdin.readline().split()

    if c[0] == "push_front":
        dq.appendleft(c[1])
    if c[0] == "push_back":
        dq.append(c[1])
    if c[0] == "pop_front":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    if c[0] == "pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    if c[0] == "size":
        print(len(dq))
    if c[0] == "empty":
        if dq:
            print(0)
        else:
            print(1)
    if c[0] == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    if c[0] == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)