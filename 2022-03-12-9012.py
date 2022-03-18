num = int(input())
for i in range(num):
    a = input()
    while "()" in a:
        a = a.replace("()","")
    if ("(" in a) or (")" in a):
        print("NO")
    else:
        print("YES")