a = [-11, 72, 9]
b = a.copy()  # shallow copy
c = list(a)  # shallow copy
d = a[:]  # shallow copy
e = a

print(a, b, c, d, e)
a[1] = 2.71
print(a, b, c, d, e)
e[0] = "ishs"
print(a, b, c, d, e)
