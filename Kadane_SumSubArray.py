# Kadane Algorithm (Largest Sum Contigous Sub Array)

# Find the subarray with the maximum sum in an array.

def Kadane(arr):
    max_so_far = arr[0]
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in arr:
        max_ending_here += i
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = arr.index(i)
        if max_ending_here < 0:
            max_ending_here = 0
            s = arr.index(i) + 1
    return arr[start:end+1]

def Kadane(arr):
    max_so_far = arr[0]
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range(len(arr)):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
    return arr[start:end+1]

# Test

a = [4, -3, -2, 2, 3, 1, -2, -3, 4, 2, -6, -3, -1, 3, 1, 2]

print(Kadane(a))
