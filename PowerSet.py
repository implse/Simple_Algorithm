# Write a function that return the powerset of a given string.

# powerSet("abcde")

# return [ ‘’, ‘a’, ‘ab’, ‘abc’, ‘abcd’, ‘abcde’, ‘abce’, ‘abd’, ‘abde’, ‘abe’, ‘ac’, ‘acd’, ‘acde’, ‘ace’, ‘ad’, ‘ade’, ‘ae’, ‘b’, ‘bc’, ‘bcd’, ‘bcde’, ‘bce’, ‘bd’, ‘bde’, ‘be’, ‘c’, ‘cd’, ‘cde’, ‘ce’, ‘d’, ‘de’, ‘e’ ]

# Iterative Solution
def powerSet_iterative(word):
    letter_list = list(word)
    power_set = [[]]
    for i in letter_list:
        power_set.extend([subset + [i] for subset in power_set])
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
    # Recursive case
    res_subsets = powerSet_recursive(word[1:])
    return res_subsets + [[word[0]]+i for i in res_subsets]

# Test
power_set_recursive = powerSet_recursive("abcde")
print(power_set_recursive)
print(len(power_set_recursive))
