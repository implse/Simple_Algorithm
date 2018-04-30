# Algorithm In Python

## Binary Search

Decrease and Conquer technique.

- Start search from the middle of the list.
- I matching value is found its index value is returned.
- If search value is not middle value :
    - move either towards left half or right half of the list.
- If value is not found, return -1.

Time Complexity :  O(log n)

## Selection Sort

- Scan the entire list to find the smallest number.
- Swaps it with the first unsorted number.
- In second iteration finds the next smallest number.
- Swaps it with number in second position.
- Repeat this process until sorted array is obtained.

Time complexity : O(n^2)
