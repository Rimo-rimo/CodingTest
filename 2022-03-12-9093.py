num = int(input())

for i in range(num):
    a = input().split()
    for k in a:
        print(k[::-1], end=" ")