# a = int(input())
# print(a//1000)

# n = int(input())
# k = int(input())
# print(k//n)

# N = int(input())
# K = int(input())
# print(N//K)

# a = int(input())
# print(a % 10)

# a = int(input())
# print(a//100%10)

# a = int(input())
# print(a // 100 + a // 10 % 10 + a // 1 % 10)

# a = int(input())
# n = int(input())
# k_100 = n // 100
# n = n - k_100 * 100
#
# k_20 = n // 20
# n = n - k_20 * 20
#
# k_10 = n // 10
# n = n - k_10 * 10
#
# k_5 = n // 5
# n = n - k_5 * 5
#
# k_1 = n // 1
# n = n - k_1 * 1
#
# print(k_100 + k_20 + k_10 + k_5 + k_1)
#

# a = int(input())
# a = a % 1440
# h = a // 60
# m = a - (a // 60)*60
# print(h, m)

# a = int(input())
# print(a - a % 2 + 2)

# a = int(input())
# a = a % 86400
# h = a // (60 ** 2)
# mm = (a - (h * 60 ** 2)) // 60
# m1 = mm // 10
# m2 = mm % 10
# ss = (a - (h * 60 ** 2) - (mm * 60))
# s1 = ss // 10
# s2 = ss % 10
# print(h, str(m1) + str(m2), str(s1) + str(s2), sep=":")
