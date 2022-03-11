# x =161

# if x % 2 == 0:
#     print("Четное")
# else:
#     print("НЕ четное")

# a = 4
# b = 22
# m = a
# if b > m:
#     m = b
# print(m)

# a = int(input())
# b = int(input())
#
# if b != 0:
#     print(a / b)
# else:
#     print("Не делится")
#     b = int(input())
#     if b == 0:
#         print("Ты не справился!")
#     else:
#         print(a / b)


# A = int(input())
# B = int(input())
# H = int(input())

# if H <= B:
#     if H >= A:
#         print("Это нормально")
#     else:
#         print("Недосып")
# else:
#     print("Пересып")

year = int(input())
if year % 400 == 0:
    print("Високосный")
elif year % 4 == 0:
    if year % 100 != 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Обычный")