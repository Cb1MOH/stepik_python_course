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


