# Heapsort - Max Heap

# Heapify
def heapify(arr, sz, i):

    largest = i  # Initialize root
    l = 2 * i + 1  # left child
    r = 2 * i + 2  # right child

    # Check if left child is greater than parent
    if l < sz and arr[i] < arr[l]:
        largest = l

    # Check if right child is greater than parent
    if r < sz and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap

        # Heapify the root.
        heapify(arr, sz, largest)

# Heapsort
def heapSort(arr):
    sz = len(arr)

    # Build a Max Heap.
    for i in range(sz, -1, -1):
        heapify(arr, sz, i)

    # One by one extract elements
    for i in range(sz - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

# Test
arr = [4, 8, 11, 25, 2, 17, 74, 51]

print("Initial array :")
print(arr)

heapSort(arr)
sz = len(arr)

print ("Sorted array :")
print(arr)
