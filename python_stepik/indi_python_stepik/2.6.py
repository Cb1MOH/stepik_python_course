# word = input()
# result = "Что Вы сказали? {0} ? Какое интересное слово".format(word)
# print(result)


# name = input()
# middle_name = input()
# result = "Здравствуйте, {1} {0}!".format(name, middle_name)
# print(result)

number = int(input())
prev_num = number - 1
next_num = number + 1
result = """Для числа {0} предыдущим будет число {1}.
Для числа {0} следующим будет число {2}.""".format(number, prev_num, next_num)
print(result)