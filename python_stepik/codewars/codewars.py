def remove_smallest(numbers):
    result = numbers[0]
    a = 0
    if len(numbers) == 0:
        return numbers
    else:
        for i in range(len(numbers)):
            if numbers[i] < result:
                a = i
        return numbers.remove(a)




print(remove_smallest([2, 2, 3, 4, 1, 2, 7, 8, 1]))
