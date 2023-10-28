numbers = list()
for i in range(0, 11):
    #print(i, end=' ')
    numbers.append(i)
print(numbers)
odd_numbers = numbers[1::2]
even_numbers = numbers[::2]
print(numbers[-2])
print(numbers[-11], numbers[0])
reverse_odd_numbers = numbers[-2::-2]
print(odd_numbers)
print(even_numbers)
print(reverse_odd_numbers)
