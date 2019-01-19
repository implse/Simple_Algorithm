# The Fisher–Yates shuffle is an algorithm for generating a random permutation of a finite sequence—in plain terms, the algorithm shuffles the sequence
import random

def shuffle(arr):
    n = len(arr)
    for i in range(n - 1):
        j = random.randint(i, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

cards = [x for x in range(1, 53)]
print(shuffle(cards))
