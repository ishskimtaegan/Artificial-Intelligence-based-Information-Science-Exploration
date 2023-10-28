trolly = ['김광석CD', '아이폰15프로']
print(trolly)
foods = ['다시마', '멸치']
trolly.append(foods)
print(trolly)
print(trolly[2][1])
# print(trolly.pop())  # 리스트의 맨 마지막 원소(['다시마', '멸치'])를 리턴 후 삭제
# print(trolly[2].pop())  # 멸치 원소를 리턴 후 삭제
print(trolly[2].pop(0))  # 다시마 원소를 리턴 후 삭제
print(trolly)
# trolly.append('다시마')
trolly[2].append('다시마')
print(trolly)
trolly[2].insert(0, '딸기')
print(trolly)

# trolly.pop(1)
# print(trolly)
# trolly.insert(1, '아이폰15')
# print(trolly)

#trolly[1:2] = '아이폰15'  # ['김광석CD', '아', '이', '폰', '1', '5', ['딸기', '멸치', '다시마']]

#trolly[1:2] = ['아이폰15']  # 아이폰15프로 -> 아이폰15
trolly[1:2] = ('아이폰15',)  # 아이폰15프로 -> 아이폰15
print(trolly)
# 3가지 삭제 방법
# print(trolly.pop(0))
# print(trolly.remove('김광석CD'))
del trolly[0]
print(trolly)
# trolly.clear()  # 리스트 원소 모두 삭제
print(trolly.index('아이폰15'))
print(trolly)
print('아이폰15' in trolly)
print('멸치' in trolly)
print('멸치' in trolly[1])
print(trolly.count('감자'))
print(trolly.count('아이폰15'))
trolly.append('아이폰15')
print(trolly)
print(trolly.count('아이폰15'))
# numbers1 = list()
# numbers2 = [-9, 0, 7]
# for i in range(0, 5):
#     numbers1.append(i)
# print(numbers1)
# numbers3 = numbers1 + numbers2
# print(numbers3)
# print(numbers1)
# numbers1.extend(numbers2)  # numbers1 = numbers1 + numbers2
# print(numbers1)
