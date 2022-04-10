# from string import ascii_lowercase
# from string import ascii_uppercase

# lower = "nopqrstuvwxyzabcdefghijklm"
# upper = "NOPQRSTUVWXYZABCDEFGHIJKLM"

# l = {i:k for i,k in zip(ascii_lowercase,lower)}
# u = {i:k for i,k in zip(ascii_uppercase,upper)}

# a = input()
# result = ""
# for i in a:
#     if i in ascii_lowercase:
#         result += l[i]
#     elif i in ascii_uppercase:
#         result += u[i]
#     else:
#         result += i

# print(result)
#==========================================================
a = input()
result =""
for i in a:
    asc = ord(i)
    if asc >=65 and asc<=90:
        if asc > 77:
            result += chr(asc-13)
        else:
            result += chr(asc+13)
    elif asc >= 97 and asc <= 122:
        if asc > 109:
            result += chr(asc-13)
        else:
            result += chr(asc+13)
    else:
        result += i
print(result )
