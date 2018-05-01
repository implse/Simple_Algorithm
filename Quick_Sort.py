# Quick sort : Time Complexity O(n log(n))

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Test
q1 = [13, 19, 24, 37, 8, 1, 3, 4, 71, 14, 40, 21, 6, 10, 7, 45, 18]
print(quickSort(q1))
