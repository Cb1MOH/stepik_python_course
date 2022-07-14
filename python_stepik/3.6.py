import requests

# r = requests.get('http://example.com')
# print(r.text)

# Task 1
# url = "https://stepic.org/media/attachments/course67/3.6.2/833.txt"
# r = requests.get(url)
# text = r.text
# text_list = text.splitlines()
#
# print(text)
# print(text_list)
# print(len(text_list))

# Task 2
# url = "https://stepic.org/media/attachments/course67/3.6.3/699991.txt"
# base_url = "https://stepic.org/media/attachments/course67/3.6.3/"
# name = ""
# result = ""
# r1 = requests.get(url)
# text = r1.text
# text = text.split()
#
# while str(text[0]) != "We":
#     name = str(text[0])
#     file = base_url + name
#     r2 = requests.get(file)
#     text = r2.text.split()
#     print(text)
#     if str(text[0]) == "We":
#         result = r2.text
# print(result)


#
# name = text1
# file1 = base_url + name
# r2 = requests.get(file1)
# text2 = r2.text
# print(text2)
#
# name = text2
# file2 = base_url + name
# r3 = requests.get(file2)
# text3 = r3.text
# print(text3)
#
# name = text3
# file4 = base_url + name
# r4 = requests.get(file4)
# text4 = r4.text
# print(text4)
#
# name = text4
# file5 = base_url + name
# r5 = requests.get(file5)
# text5 = r5.text
# print(text5)
