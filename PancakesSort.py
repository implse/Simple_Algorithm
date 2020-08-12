# Time Complexity O(n2) / Space Complexity 0(1)
def pancake_sort(lst):
    for size in reversed(range(len(lst))):
        max_ind = max_pos(lst[:size + 1])
        reverse(lst, 0, max_ind)
        print(lst)
        reverse(lst, 0, size)
    return lst

def max_pos(lst):
    return lst.index(max(lst))

def reverse(lst, i, j):
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

lst = [30, 25, 20, 35, 40, 45]
lst = [1, 2, 5, 3, 7]
print(pancake_sort(lst))
