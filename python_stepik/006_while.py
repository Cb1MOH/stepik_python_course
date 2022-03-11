# c = 1
# while c <= 9:
#     print('*' * c)
#     c += 1

# n = int(input())
# stars = '*'
# while len(stars) <= n:
#     print(stars)
#     stars += '*'

# s = 0
# i = 1
# while i <= 10:
#     s += i
#     i += 1
# print(s)

# a = int(input())
# s = 0
# while a != 0:
#     s += a
#     a = int(input())
# print(s)

# a = int(input())
# b = int(input())
# d = 1
#
# while d % a != 0 or d % b != 0:
#     d += 1
# print(d)

a = 0
while a <= 100:
    a = int(input())
    if a < 10:
        continue
    if a > 100:
        break
    print(a)
