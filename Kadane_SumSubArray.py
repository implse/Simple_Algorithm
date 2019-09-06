# Kadane Algorithm (Largest Sum Contiguous Sub Array)

from sys import maxsize

# Find the contiguous sub array with the maximum sum
def findmaxSumSubArray(arr):
    # max_so_far = arr[0]
    max_so_far = maxsize * -1
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

# Find the maximum sum of contiguous sub array
def findMaxSum(arr):
        # max_so_far = arr[0]
        max_so_far = maxsize * -1
        max_ending_here = 0
        for i in range(len(arr)):
            max_ending_here += arr[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

# Test 1
a = [4, -3, -2, 2, 3, 1, -2, -3, 4, 2, -6, -3, -1, 3, 1, 2]
print('The maximum subarray sum is : {}'.format(findMaxSum(a)))
print('The maximum sum subarray is : {}'.format(findmaxSumSubArray(a)))

# Test 2
b = [-5, 6, 7, 1, 4, -8, 16]
print('The maximum subarray sum is : {}'.format(findMaxSum(b)))
print('The maximum sum subarray is : {}'.format(findmaxSumSubArray(b)))

# Test 3
c =  [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print('The maximum subarray sum is : {}'.format(findMaxSum(c)))
print('The maximum sum subarray is : {}'.format(findmaxSumSubArray(c)))
