# Task_1
# def update_dictionary(d, key, value):
#     if key not in d:
#         if d[2 * key] not in d:
#             d[2 * key] = [value]
#         else:
#             d[2 * key] = [int(x) for x in str(d[2 * key])]
#             d[2 * key].append(value)
#     else:
#         d[key] = [int(x) for x in str(d[key])]
#         d[key].append(value)

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        if (key * 2) in d:
            d[key * 2].append(value)
        else:
            d[key * 2] = [value]


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}

# di = {"one": 1, "two": 2, "three": 3}
# di["one"] = [int(x) for x in str(di["one"])]
# di["one"].append(2)
#
# print(di)
