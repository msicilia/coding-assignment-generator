def sum_lists(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result

# Test cases:
print(sum_lists([1, 2, 3], [4, 5, 6])) # Expected output [5, 7, 9]
print(sum_lists([0, -1, -2], [1, 2, 3])) # Expected output [1, 1, 1]
print(sum_lists([], [])) # Expected output []