# a = input()
#
# G = a.upper().count('G')
# C = a.upper().count('C')
# L = len(a)
# result = (C + G) / L * 100
# print(result)


inputString = 'aaaabbcaa'
countLetters = 0
position = 0

for i in inputString:
    if i == inputString[position]:
        countLetters += 1
        position += 1
    if i != inputString[position]:
        print(i + str(countLetters), end='')
        countLetters = 0













    # while a[b] == i:
    #     b += 1
    #     count += 1
    #
