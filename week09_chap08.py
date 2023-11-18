subjects1 = {'python': 5, 'java': 9}
subjects2 = {'data structure': 5, 'java': 9, 'go': [7, 8]}
subjects3 = subjects2
subjects4 = dict(subjects2)
subjects = {**subjects1, **subjects2}
print(subjects)
subjects2['java'] = 11
subjects2['go'][0] = 12
print(subjects)
print(subjects1)
print(subjects2)
print(subjects3)
print(subjects4)
