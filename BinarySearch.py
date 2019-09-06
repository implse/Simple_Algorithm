# Binary Search : Time Complexity O(log n)

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2 # Avoid Overflow
        value = list[mid]
        if value == item:
            return "The item %d is at index: %d" % (item, mid)
        if value > item:
            high = mid - 1
        else:
            low = mid + 1
    return "The item %d is not in the list." % (item)

# Test
b1 = [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]
print(binary_search(b1, 38))
