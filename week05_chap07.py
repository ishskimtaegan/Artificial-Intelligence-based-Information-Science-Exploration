t1 = ()
t2 = ('ishs') # str
t3 = 'ishs',
t4 = ('ishs',)
t5 = ('ishs', 'python', 'java')
t6 = 'ishs', 'python', 'java'
print(type(t1))
print(type(t2))
print(type(t3))
print(type(t4))
print(type(t5))
print(t5[1])  # same as list indexing
print(type(t6))
print(type('test',))  # str
print(type(('test',)))  # tuple
