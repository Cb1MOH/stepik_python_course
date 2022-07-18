#Task_1
# A = int(input())
# B = int(input())
# H = int(input())
# if A <= H <= B:
#     print('Это нормально')
# elif H < A:
#     print('Недосып')
# elif H > B:
#     print('Пересып')

#Task_2
year = int(input())
if year % 400 == 0:
    print('Високосный')
elif year % 4 == 0 and year % 100 != 0:
    print('Високосный')
else:
    print('Обычный')



# year = int(input())
# if year % 400 == 0:
#     print("Високосный")
# elif year % 4 == 0:
#     if year % 100 != 0:
#         print("Високосный")
#     else:
#         print("Обычный")
# else:
#     print("Обычный")