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

# Task 2
# formatted_body = ""
# words_list = []
# count_words = {}
# with open("data/dataset_3363_4.txt") as text:
#     body = text.read()
#     for i in body:
#         if i in "!@#$%^&*(){}:\"?><.,":
#             formatted_body += ""
#         else:
#             formatted_body += i
#     words_list = formatted_body.lower().split()
#     for word in words_list:
#         if word in count_words:
#             count_words[word] += 1
#         else:
#             count_words[word] = 1
#     find_max = max(count_words, key=count_words.get)
#
#     print(find_max + " " + str(count_words[find_max]))
#     print(words_list)

# Task 3
# with open("data/dataset_3363_4.txt", "r", encoding="utf-8") as text:
#     people_and_marks = {}
#     readline = text.read().splitlines()
#     for i in readline:
#         split_line = i.split(";")
#         people_and_marks[split_line[0]] = [split_line[1], split_line[2], split_line[3]]
#     for i in people_and_marks.keys():
#         print((int(people_and_marks[i][0]) + int(people_and_marks[i][1]) + int(people_and_marks[i][2])) / 3)
#     students_quantity = len(people_and_marks.keys())
#     math = 0
#     phiz = 0
#     rus = 0
#     x = 0
#     for i in people_and_marks.values():
#         math += int(i[0])
#         phiz += int(i[1])
#         rus += int(i[2])
#     print(math / students_quantity, end=" ")
#     print(phiz / students_quantity, end=" ")
#     print(rus / students_quantity, end=" ")
