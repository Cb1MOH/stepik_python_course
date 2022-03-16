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
# number_of_developers = input()
# number_of_developers_int = int(number_of_developers)
# core = ' программист'
# end_1 = ''
# end_2 = 'а'
# end_3 = 'ов'
# if number_of_developers_int % 10 == 0 or 5 <= (number_of_developers_int % 10) <= 9 \
#         or 10 <= number_of_developers_int <= 19 or 11 <= (number_of_developers_int % 100) <= 19:
#     print(number_of_developers + core + end_3)
# elif number_of_developers_int % 10 == 1 and number_of_developers_int % 100 != 11:
#     print(number_of_developers + core)
# elif 2 <= (number_of_developers_int % 10) <= 4 and (number_of_developers_int % 100) != 12 \
#         and (number_of_developers_int % 100) != 13 and (number_of_developers_int % 100) != 14:
#     print(number_of_developers + core + end_2)
    




# number = int(input())
# lastDigit = number % 10
# lastTwoDigits = number % 100
# if number == 0 or 5 <= lastTwoDigits <= 19 or lastDigit == 0 or 5 <= lastDigit <= 9:
#     print(str(number) + " " + "программистов")
# elif lastDigit == 1:
#     print(str(number) + " " + "программист")
# elif 2 <= lastDigit <= 4:
#     print(str(number) + " " + "программиста")