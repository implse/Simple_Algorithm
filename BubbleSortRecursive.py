# Bubble Sort : Time Complexity O(n^2)
def bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

# Buble Sort Recursive
def bubble_sort(data):
    n = len(data)
    def bubble_sort_recursive(data, n):
        # Base Case
        if n == 1:
            return
        for i in range(n - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        # Recursive Case
        bubble_sort_recursive(data, n - 1)
    # Function call
    bubble_sort_recursive(data, n)
    return data
