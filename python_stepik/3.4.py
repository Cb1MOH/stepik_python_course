# Task 1
# with open("data/dataset_3363_2.txt") as text:
#     s1 = text.readline()
#     general = ""
#     char = ""
#     num = ""
#     num_list = []
#     index = 0
#
#     for i in s1:
#         if i.isalpha():
#             char += i
#             num += " "
#         else:
#             char += " "
#             num += i
#     char = char.split()
#     num = num.split()
#
#     for i in num:
#         num_list.append(int(i))
#
#     for i in char:
#         general += i * num_list[index]
#         index += 1
#     print(general)
