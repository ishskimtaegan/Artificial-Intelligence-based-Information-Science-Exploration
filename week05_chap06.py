index = 0
numbers = [9, 0, 11, -3, 55, 0]
# print(numbers[4])  # 55
while index < len(numbers):
    number = numbers[index]
    if number < 0:
        print('음수 발견!', number)
        break
    print(index)
    index = index + 1
else:
    print('음수를 찾지 못했습니다')