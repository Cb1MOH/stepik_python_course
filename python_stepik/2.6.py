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
    # print(start_list)
    # print(sorted_list)
    # print(sorted_list_of_lists)
