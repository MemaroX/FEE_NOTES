def second_largest(x):
    if len(x) < 2:
        return None
    largest = second_largest = float('-inf')
    for i in x:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    if second_largest == float('-inf'):
        return None
    return second_largest

# Test the function
list1 = [10, 20, 4]
print(second_largest(list1))  # Output: 10

list2 = [70, 11, 20, 4, 100]
print(second_largest(list2))  # Output: 70



def chars_mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b

# Test the function
print(chars_mix_up("abc", "xyz"))  # Output: "xyc abz"
