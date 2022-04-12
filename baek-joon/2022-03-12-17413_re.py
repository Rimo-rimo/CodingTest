sen = input()
re = ""
now = ">"
item = ""
for i in sen:
    if i == "<":
        now = "<"
        if item:
            re += "".join(reversed(item))
        item = i
    elif i == ">":
        now = ">"
        re += (item+i)
        item = ""
    elif now == ">" and i == " ":
        re += "".join(reversed(item))+i
        item = ""
    else:
        item += i
if item:
    re += "".join(reversed(item))
print(re)

