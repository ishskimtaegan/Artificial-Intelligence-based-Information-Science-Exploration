x = [1, 2, 3]
y = x
print(x, y)
y[0] = -11
print(x, y)
# dictionary : mutable
human = {'eye': [1.0, 0.9], 'blood_type': 'ab'}
print(human['eye'])
human['eye'][0] = 0.7
print(human['eye'])
print(f"혈액형은 {human['blood_type']}형 입니다")


# a = 1
# b = a
# print(a, b)
# a = 2
# print(a, b)

# a = 5.1
# b = 12.3 - a
# print(b)
# print(id(a), id(b))