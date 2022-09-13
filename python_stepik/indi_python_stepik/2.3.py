# a = input()
# print(a.upper())

# a = input()
# print(a.lower().count("e"))


# a = input()
# print(a.replace("w", "").replace("z", ""))

# a = input()
# print(a.find("a"))

# a = input()
# print(a.rfind("a"))

# a = input()
# print(len(a.split()))

# a = input()
# print(a.replace(" ", ","))

# a = input()
# print(a[0:3].upper() + a[3:-3].lower() + a[-3:].upper())

a = input()
b = a.lower().replace("a", "").replace("o", "").replace("y", "").replace("e", "").replace("u", "").replace("i", "")
b = ".".join(b)
print("." + b)