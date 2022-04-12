from collections import Counter
from string import ascii_lowercase

alpha = ascii_lowercase
a = input()
for i in alpha:
    print(a.count(i), end=" ")
