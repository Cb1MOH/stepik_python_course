# Task_1
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#     else:
#         if (key * 2) in d:
#             d[key * 2].append(value)
#         else:
#             d[key * 2] = [value]
#
#
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}


# Task 2
# the_string = input()
# words_list = the_string.lower().split()
# result = {}
# for i in words_list:
#     if i in result.keys():
#         result[i] += 1
#     else:
#         result[i] = 1
# for key, value in result.items():
#     print(key, value)
