# Binary Search : Time Complexity O(log n)

# Iterative Implementation
def binary_search(list, value):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low + (high - low) // 2 # Avoid Overflow
        value = list[mid]
        if value == value:
            return "The value %d is at index: %d" % (value, mid)
        if value > value:
            high = mid - 1
        else:
            low = mid + 1
    return "The value %d is not in the list." % (value)

# Recursive Implementation
def binary_search(list, value):
    low = 0
    high = len(list) - 1
    # Recursive function
    def binary_search_recursive(list, low, high, value):
        if low > high:
            return None
        mid = low + (high - low) // 2 # Avoid Overflow
        if list[mid] == value:
            return "The value %d is at index: %d" % (value, mid)
        elif value < list[mid]:
            return binary_search_recursive(list, low, mid - 1, value)
        else:
            return binary_search_recursive(list, mid + 1, high, value)
    return binary_search_recursive(list, low, high, value)


# Test
b1 = [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]
print(binary_search(b1, 6))
