# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# print(students)

# Task_1
# a = [int(i) for i in input().split()]
# s = 0
# for i in a:
#     s += i
# print(s)

# Task_2
# a = [int(i) for i in input().split()]
# b = []
# count = 1
# c = ''
# if len(a) == 1:
#     c = str(a[0])
#     print(c)
# else:
#     b.append(a[-1] + a[1])
#     for i in a[1:-1]:
#         b.append(a[count - 1] + a[count + 1])
#         count += 1
#     b.append(a[-2] + a[0])
#     for i in b:
#         c = c + str(i) + ' '
#     print(c)
