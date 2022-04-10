# import sys
# import string
# from collections import Counter

# while True:
#     try:
#         a = input()
#         l,u,n,s = 0,0,0,0
#         for i in a:
#             if i in string.ascii_lowercase:
#                 l+=1
#             elif i in string.ascii_uppercase:
#                 u+=1
#             elif i in "0123456789":
#                 n+=1
#             else:
#                 s+=1
#         print(l,u,n,s)
#     except EOFError:
#         break

while True:
    try:
        a = input()
        lower = sum(i.islower() for i in a)
        upper = sum(i.isupper() for  i in a)
        num = sum(i.isdigit() for i in a)
        blank = sum(i.isspace() for i in a)
        print(lower, upper, num, blank)
    except EOFError:
        break
