# Selection Sort : Time Complexity O(n^2)

def selectionSort(array):
    for i in range(0, len(array) - 1):
        minIndex = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        if minIndex != i:
            array[i], array[minIndex] = array[minIndex], array[i]
    return array

# Test
s1 = [13, 19, 24, 37, 8, 1, 3, 4, 71, 14, 40, 21, 6, 10, 7, 45, 18]
print(selectionSort(s1))
