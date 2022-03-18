p = input()
p = p.replace("()", "#")
num_state = 0
result = 0
for i in p:
    if i == "(":
        num_state += 1
        result += 1

    if i == ")":
        num_state -= 1

    if i == "#":
        if num_state != 0:
            result += num_state
print(result)