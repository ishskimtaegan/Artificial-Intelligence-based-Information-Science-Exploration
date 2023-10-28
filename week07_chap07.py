fruits = ['딸기', '망고', '포도', '사과', '골드키위']
print(fruits)
fruits_string = ' / '.join(fruits)  # 리스트의 원소들을 문자열로 변환
print(fruits_string)
school = 'Incheon Science High School'
school_list = school.split()  # 문자열을 리스트로 변환. 구분자 기본 값은 띄어쓰기
#school_list = school.split('S')  # 문자열을 리스트로 변환. 구분자는 'S'
print(school_list)
#school_list.sort()  # 오름차순, 원본 자체를 정렬
#school_list.sort(reverse=True)  # 내림차순, 원본 자체를 정렬
sorted_school_list = sorted(school_list)  # 원본은 그대로 두고 사본을 오름차순 정렬
print(sorted_school_list)
print(school_list, len(school_list))