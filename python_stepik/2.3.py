# Task_1
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print('', end='\t')
# for g in range(c, d + 1):
#     print(g, end='\t')
# print('')
# for i in range(a, b + 1):
#     print(i, end='\t')
#     for j in range(c, d + 1):
#         print(i * j, end='\t')
#     print('\t')

# Вывусти сумму всех нечетных чисел от a до b(включая обе границы)
# a,b = input().split()
# a = int(a)
# b = int(b)
# sum = 0
# for i in range(a, b+1):
#     if i % 2 == 1:
#         sum += i
#     print(i)
# print(sum)

# a, b = input().split()
# a = int(a)
# b = int(b)
# s = 0
# if a % 2 != 1:
#     a += 1
# for i in range(a, b + 1, 2):
#     s += i
# print(s)

# Task_2
# a = int(input())
# b = int(input())
# # a, b = (float(i) for i in input().split())
# s = 0
# count = 0
# while a % 3 != 0:
#     a += 1
# for i in range(a, b + 1, 3):
#     s += i
#     count += 1
# print(s / count)
