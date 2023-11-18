#subjects = dict(python=5, java=9)  # subjects = {'python': 5, 'java': 9}
subjects = [['python', 5], ['java', 9]]  # 2d list
subjects = dict(subjects)  # transform 2d list to dictionary

print(subjects)
print(subjects['java'])  # access
subjects['go'] = 7  # add
print(subjects)
subjects['java'] = 8  # update
print(subjects)

for subject in subjects:  # print key values
    print(subject)

for subject in subjects.values():  # print values
    print(subject)

for subject in subjects.keys():  # print key values
    print(subject)

for subject in subjects.items():  # print key and values in tuple form, (key, value)
    print(subject)

for subject, students in subjects.items():  # unpacking tuples
    #print(subject, students)
    print(f"{subject} 과목을 수강하는 학생의 인원은 {students}명 입니다")

del subjects['java']  # delete
print(subjects)
