numbers = list()
for i in range(0, 11):
    numbers.append(i)
print(numbers)
reverse_numbers = numbers[::-1]
print(reverse_numbers)
print(numbers)
numbers.reverse()  # 자체 값 변경
print(numbers)
