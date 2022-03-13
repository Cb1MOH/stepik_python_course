# Task_1
# a = int(input())
# b = int(input())
# c = int(input())
#
# p = (a + b + c) / 2
# S = (p * (p-a)*(p-b)* (p-c)) ** 0.5
# print(S)

# Task_2
# a = int(input())
# if -15 < a <= 12 or 14<a<17 or 19 <=a:
#     print('True')
# else:
#     print('False')

# Task_3
# a = float(input())
# b = float(input())
# c = input()
#
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif c == '/':
#     if b == 0:
#         print('Деление на 0!')
#     else:
#         print(a / b)
# elif c == 'mod':
#     if b == 0:
#         print('Деление на 0!')
#     else:
#         print(a % b)
# elif c == 'pow':
#     print(a ** b)
# elif c == 'div':
#     if b == 0:
#         print('Деление на 0!')
#     else:
#         print(a // b)


# Task_4
# figure = input()
# if figure == 'треугольник':
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2
#     S = (p * (p - a)* (p - b) * (p - c)) ** 0.5
#     print(float(S))
# elif figure == 'прямоугольник':
#     a = int(input())
#     b = int(input())
#     S = a * b
#     print(float(S))
# elif figure == 'круг':
#     r = int(input())
#     S = 3.14 * r ** 2
#     print(float(S))

# # Task_5
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a >= b and a >= c:
#     print(a)
#     if b < c:
#         print(b)
#         print(c)
#     else:
#         print(c)
#         print(b)
#
# elif b >= a and b >= c:
#     print(b)
#     if a < c:
#         print(a)
#         print(c)
#     else:
#         print(c)
#         print(a)
#
# elif c >= b and c >= a:
#     print(c)
#     if b < a:
#         print(b)
#         print(a)
#     else:
#         print(a)
#         print(b)

# Task_6
numberOfDevelopers = input()
core = ' программист'
end1 = ''
end2 = 'а'
end3 = 'ов'
if int(numberOfDevelopers) == 1:
    print(numberOfDevelopers + core)
elif int(numberOfDevelopers) == 2 or int(numberOfDevelopers) == 3 or int(numberOfDevelopers) == 4:
    print(numberOfDevelopers + core + end2)
elif 5 <= int(numberOfDevelopers) <= 20 or int(numberOfDevelopers) == 0:
    print(numberOfDevelopers + core + end3)
elif int(numberOfDevelopers[-1]) == 0 or int(numberOfDevelopers[-1]) == 5 or int(numberOfDevelopers[-1]) == 6 or int(numberOfDevelopers[-1]) == 7 or int(numberOfDevelopers[-1]) == 8 or int(numberOfDevelopers[-1]) == 9:
    print(numberOfDevelopers + core + end3)
elif int(numberOfDevelopers[-1]) == 1:
    print(numberOfDevelopers + core)
elif int(numberOfDevelopers[-1]) == 2 or int(numberOfDevelopers[-1]) == 3 or int(numberOfDevelopers[-1]) == 4:
    print(numberOfDevelopers + core + end2)

# number = int(input())
# lastDigit = number % 10
# lastTwoDigits = number % 100
# if number == 0 or 5 <= lastTwoDigits <= 19 or lastDigit == 0 or 5 <= lastDigit <= 9:
#     print(str(number) + " " + "программистов")
# elif lastDigit == 1:
#     print(str(number) + " " + "программист")
# elif 2 <= lastDigit <= 4:
#     print(str(number) + " " + "программиста")