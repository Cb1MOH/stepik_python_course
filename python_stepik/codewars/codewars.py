# def compare(string, ending):
#     index = -1
#     count = min(len(string), len(ending))
#     result = True
#     if len(ending) <= len(string):
#         for i in range(count):
#             if string[index] == ending[index]:
#                 result = True
#                 index -= 1
#             else:
#                 result = False
#     else:
#         result = False
#     return result
#
#
# print(compare('sumo', 'smo'))
# print(compare('ails', 'fails'))


# def is_square(n):
#     result = True
#     if n < 0:
#         result = False
#     else:
#         number = n ** 0.5
#         number = int(number)
#         if number ** 2 == n:
#             result = True
#         else:
#             result = False
#     return result
#
#
# print(is_square(-1))
# print(is_square(0))


# def cockroach_speed(s):
#     result = s * (100000/3600)
#     return int(result)
#
#
# print(cockroach_speed(72))
# print(cockroach_speed(108))
# print(cockroach_speed(0))
# print(cockroach_speed(1.08))
# print(cockroach_speed(1.09))

# def better_than_average(class_points, your_points):
#     sum_of_elements = 0
#     quontity = 0
#     for i in class_points:
#         sum_of_elements += i
#         quontity += 1
#     sum_of_elements += your_points
#     quontity += 1
#     result = sum_of_elements / quontity
#     if your_points > result:
#         return True
#     else:
#         return False
#
#
# print(better_than_average([2, 3], 5))

# def smash(words):
#     result = ""
#     for i in words:
#         result = result + i + " "
#     return result[:-1]
#
#
# words = ['hello', 'world', 'this', 'is', 'great']
# print(smash(words))


# def number(lines):
#     line_number = 1
#     result = []
#     if len(lines) == 0:
#         return result
#     for i in lines:
#         result.append(str(line_number) + ": " + i)
#         line_number += 1
#     return result
#
#
# lines = []
# print(number(lines))

# def get_middle(s):
#     if len(s) % 2 != 0:
#         result = s[(len(s) - 1) // 2]
#     else:
#         result = s[((len(s) - 2) // 2):((len(s) + 2) // 2)]
#     return result
#
#
# s = "123456"
# print(get_middle(s))
#
# a = [5, 8, 4, 3, 5, 7]
# value = a[0]
# for i in a:
#     if i < value:
#         value = i
# print(value)
# a = "2"
# b = str(a)
# c = list(b)
# print(c)