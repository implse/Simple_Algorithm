def permutations(lst):
    result = list()
    chosen = list()
    permutionsHelper(lst, result, chosen)
    return result

def permutionsHelper(lst, result, chosen = []):
    if len(lst) == 0:
        result.append(chosen.copy())
    else:
        for i in range(len(lst)):
            c = lst[i]
            chosen.append(c)
            lst.pop(i)
            permutionsHelper(lst, result, chosen)
            chosen.pop()
            lst.insert(i, c)

# Test
l = [1, 2, 3]
print(permutations(l))
