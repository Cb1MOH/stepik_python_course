# a = [5, 8, 4, 3, 5, 7]
# element = a[0]
# for i in a:
#     if i < element:
#         element = i
# print(element)

# Task_1
# a = int(input())
# s = 0
# s += a
# numbers = []
# numbers.append(a ** 2)
# sum_of_qw = 0
# if a == 0:
#     print(a)
# else:
#     while s != 0:
#         a = int(input())
#         s = s + a
#         numbers.append(a ** 2)
#     for i in numbers:
#         sum_of_qw += i
#     print(sum_of_qw)

# Task_2
# inpt = int(input())
# a = ''
# count = inpt
# start_list = []
# sorted_list = []
# sorted_list_of_lists = []
# result = []
# if inpt == 0:
#     print(inpt)
# else:
#     while count != 0:
#         start_list.append(count)
#         count -= 1
#     start_list.sort()
#     for i in start_list:
#         sorted_list.append([i])
#     for i in sorted_list:
#         for j in i:
#             sorted_list_of_lists.append([j] * j)
#     while len(result) <= inpt:
#         for i in sorted_list_of_lists:
#             for j in i:
#                 result.append(j)
#     print(*result[:inpt])

# Task_3
# lst = [int(i) for i in input().split()]
# upd_lst = lst
# x = int(input())
# lst_of_indx = []
# if x not in lst:
#     print('Отсутствует')
# while x in upd_lst:
#     indx = upd_lst.index(x)
#     lst_of_indx.append(indx)
#     upd_lst.insert(indx, 0)
#     del upd_lst[indx + 1]
# print(*lst_of_indx)

# Task_4
# TODO finish the task https://stepik.org/lesson/3369/step/10?unit=952


# Soper
# n, m, k = 5, 5, 3
# # # n, m, k = (int(i) for i in input().split())
# a = [[0 for j in range(m)] for i in range(n)]
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()
