from collections import deque
import sys

queue = deque()
num = int(sys.stdin.readline())
for i in range(num):
    c = sys.stdin.readline().split()
    if c[0] == "push":
        queue.append(c[1])
    if c[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    if c[0] == "size":
        print(len(queue))
    if c[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    if c[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    if c[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)