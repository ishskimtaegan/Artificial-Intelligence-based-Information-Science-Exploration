subjects = {'python': 5, 'java': 9}
print(subjects)
print(subjects['java'])  # access
subjects['go'] = 7  # add
print(subjects)
subjects['java'] = 8  # update
print(subjects)

for subject in subjects:  # 키 값들만 출력
    print(subject)

for subject in subjects.values():  # 값들만 출력
    print(subject)

for subject in subjects.keys():  # 키 값들만 출력
    print(subject)

for subject in subjects.items():  # (key, value) 튜플로 리턴
    print(subject)

for subject, students in subjects.items():  # 튜플 unpacking 후 리턴
    #print(subject, students)
    print(f"{subject} 과목을 수강하는 학생의 인원은 {students}명 입니다")

del subjects['java']  # delete
print(subjects)
