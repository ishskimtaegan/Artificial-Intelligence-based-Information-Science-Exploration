subjects = [['python', 5], ['java', 9], ['go', 7]]  # 2d list
subjects = dict(subjects)  # transform 2d list to dictionary

print(subjects['go'])
print(subjects.get('go'))
print(subjects.values())
print(list(subjects.values()))
print(len(subjects))