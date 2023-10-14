subjects = ('python', 'english', 'math')  # packing
print(subjects)
print(type(subjects))
print(subjects[1])
#s1, s2, s3, s4 = subjects  # not enough values to unpack (expected 4, got 3)
#s1, s2 = subjects  # too many values to unpack (expected 2)
s1, s2, s3 = subjects  # unpacking
print(s2)