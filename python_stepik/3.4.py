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

# Task 3
formatted_body = ""
words_list = []
count_words = {}
with open("data/dataset_3363_3.txt") as text:
    body = text.read()
    for i in body:
        if i in "!@#$%^&*(){}:\"?><.,":
            formatted_body += ""
        else:
            formatted_body += i
    words_list = formatted_body.lower().split()
    for word in words_list:
        if word in count_words:
            count_words[word] += 1
        else:
            count_words[word] = 1
    find_max = max(count_words, key=count_words.get)

    print(find_max + " " + str(count_words[find_max]))
    print(words_list)