a = [-11, [3, 0], 9]
#a = [-11, 72, 9]
b = a.copy()  # shallow copy
c = list(a)  # shallow copy
d = a[:]  # shallow copy
e = a

print(a, b, c, d, e)
a[1][0] = 7
#a[1] = 99
print(a, b, c, d, e)
