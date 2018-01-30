# Generating permutation using Heap's Algorithm

# heapPermutation takes two parameters :
    # - the list to do all the permutations.
    # - the length of the list

# 1 : Print to the console all the permutations.
def heapPermutation(lst, n):
    # Swap function
    def swap(list, index1, index2):
        list[index1], list[index2] = list[index2], list[index1]

    if n == 1:
        print(lst)
    else:
        for i in range(0, n - 1):
            heapPermutation(lst, n - 1)
            if(n % 2 == 0):
                swap(lst, i, n - 1)
            else:
                swap(lst, 0, n - 1)

        heapPermutation(lst, n - 1)

# Test 1
lst = ['a', 'b', 'c', 'd']
ln = len(lst)
print(heapPermutation(lst, ln))

# 2: Return an array of all the permutations.
import copy
def allPermutations(data, n):
    permutations = []
    # Simple swap list values function
    def swap(arr, index1, index2):
        arr[index1], arr[index2] = arr[index2], arr[index1]
    # Permutations function
    def heapPermutation(data, n):
        if n == 1:
            a = copy.deepcopy(data)
            permutations.append(a)
        else:
            for i in range(0, n-1):
                heapPermutation(data, n-1)
                if n%2 == 0:
                    swap(data, i, n-1)
                else:
                    swap(data, 0, n-1)
            heapPermutation(data, n-1)
    heapPermutation(data, n)
    return permutations

# Test 2
lst2 = ['a', 'b', 'c', 'd']
ln = len(lst2)
perm = allPermutations(lst2, ln)
for p in perm:
    print(p)
