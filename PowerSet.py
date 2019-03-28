# powerSet When an string is passed in the function, it will return all the subsets and combination in an array

# powerSet("abcde")

# return [ ‘’, ‘a’, ‘ab’, ‘abc’, ‘abcd’, ‘abcde’, ‘abce’, ‘abd’, ‘abde’, ‘abe’, ‘ac’, ‘acd’, ‘acde’, ‘ace’, ‘ad’, ‘ade’, ‘ae’, ‘b’, ‘bc’, ‘bcd’, ‘bcde’, ‘bce’, ‘bd’, ‘bde’, ‘be’, ‘c’, ‘cd’, ‘cde’, ‘ce’, ‘d’, ‘de’, ‘e’ ]

# Iterative Solution
def powerSet_iterative(word):
    # This loop is to take out all duplicate
    letter_list = list(word)
    power_set = [" "]

    for i in range(len(letter_list)):
        # Prevent an infinite loop
        ln = len(power_set)
        for j in range(ln):
            power_set.append(power_set[j]+letter_list[i])
    return power_set

# Test
power_set_iterative = powerSet_iterative("abcde")
print(power_set_iterative)
print(len(power_set_iterative))

# Recursive Solution
def powerSet_recursive(word):
    # Base case
    if not word:
        return [[]]
    res_subsets = powerSet_recursive(word[1:])
    return res_subsets + [[word[0]]+i for i in res_subsets]

# Test
power_set_recursive = powerSet_recursive("abcde")
print(power_set_recursive)
print(len(power_set_recursive))
