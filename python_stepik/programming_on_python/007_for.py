# a = 1
# b = 3
# c = 2
# d = 4
#
# for i in range(c, d + 1):
#     print('', end='\t')
#     print(i, end='\t')
# print()
# for i in range(a, b + 1):
#     for j in range(c, d + 1):
#         print(j, end='\t')
#     print()
#
# for i in range(10 + 1):
#     for j in range(i):
#         print(j, end=' ')
#     print()

# a = int(input())
# b = int(input())
# s = 0
# if a % 2 != 0:
#     a += 1
# else:
#     for i in range(a, b + 1, 2):
#             s += i
# print(s)


a = int(input())
b = int(input())
c = 0
number = 0
total = 0

for i in range(a, b +1):
    if i % 3 == 0:
        c += i
        number += 1
total = c / number
print(total)