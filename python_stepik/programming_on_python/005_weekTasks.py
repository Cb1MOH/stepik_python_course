# a = int(input())
# b = int(input())
# c = int(input())
#
# p = (a + b + c) / 2
# s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(s)



# a = int(input())
#
# if -15 < a <= 12 or 14 < a < 17 or 19 <= a:
#     print("True")
# else:
#     print("False")


# a = float(input())
# b = float(input())
# c = input()
#
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '/':
#     if b == 0:
#         print("Деление на 0!")
#     else:
#         print(a / b)
# elif c == '*':
#     print(a * b)
# elif c == 'mod':
#     if b == 0:
#         print("Деление на 0!")
#     else:
#         print(a % b)
# elif c == 'pow':
#     print(a ** b)
# elif c == 'div':
#     if b == 0:
#         print("Деление на 0!")
#     else:
#         print(a // b)



# figure = input()
#
# if figure == "треугольник":
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2
#     s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     print(s)
# elif figure == "прямоугольник":
#     a = int(input())
#     b = int(input())
#     s = a * b
#     print(s)
# elif figure == "круг":
#     r = int(input())
#     pi = 3.14
#     s = pi * r ** 2
#     print(s)

# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# elif c > a and c > b:
#     print(c)
# elif a < b and a < c:
#     print(a)
# elif b < a and b < c:
#     print(b)
# elif c < a and c < b:
#     print(c)
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
# elif b >= a and b >= c:
#     print(b)
#     if a < c:
#         print(a)
#         print(c)
#     else:
#         print(c)
#         print(a)
# else:
#     print(c)
#     if b < a:
#         print(b)
#         print(a)
#     else:
#         print(a)
#         print(b)


# number = int(input())
# lastDigit = number % 10
# lastTwoDigits = number % 100
# if number == 0 or 5 <= lastTwoDigits <= 19 or lastDigit == 0 or 5 <= lastDigit <= 9:
#     print(str(number) + " " + "программистов")
# elif lastDigit == 1:
#     print(str(number) + " " + "программист")
# elif 2 <= lastDigit <= 4:
#     print(str(number) + " " + "программиста")

# ticket_number = int(input())
# ticket_number_int = int(ticket_number)
# sum_last_three_digits = ticket_number_int // 10**0 % 10 + ticket_number_int // 10**1 % 10 + ticket_number_int // 10**2 % 10
# sum_first_three_digits = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
# if sum_first_three_digits == sum_last_three_digits:
#     print("Счастливый")
# else:
#     print("Обычный")

# sum_first_three_digits = ((ticket_number // 100000) % 10) + ((ticket_number // 100000) % 10) + ((ticket_number // 100000) % 10)
# sum_last_three_digits = ticket_number_int // 10**0 % 10 + ticket_number_int // 10**1 % 10 + ticket_number_int // 10**2 % 10
# if sum_first_three_digits == sum_last_three_digits:


# print(ticket_number_int // 100000)
# print(ticket_number_int // 10000)
# print(ticket_number_int // 1 % 10)


