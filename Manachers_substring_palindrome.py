# Given a input string finds the longest substring palindrome

# Manacher's Algorithm O(n)
def update_string(string):
    newString = ["#"]
    for char in string:
        newString += ["#", char]
    return "".join(newString)

def manacher(string):
    string = update_string(string)
    LPS = [0 for _ in range(len(string))]
    C = 0
    R = 0
    for i in range(len(string)):
        i_mirror = 2 * C - i
        if R > i:
            LPS[i] = min(R - i, LPS[i_mirror])
        else:
            LPS[i] = 0
        try:
            while string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
                LPS[i] += 1
        except:
            pass
        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]
    max_LPS = max(LPS)
    r, c = max_LPS, LPS.index(max_LPS)
    print(string[c - r : c + r].replace("#", ""))
    return r

str = "mollakayakokomassa"
print(manacher(str))

# Brute Force
def longest_palindrome(string):
    ln = len(string)
    max_size_palindrome = 0
    palindrome = ""
    for i in range(ln - 1):
        for j in range(i + 1, ln):
            str1 = string[i:j]
            str2 = str1[::-1]
            if str1 == str2 and len(str1) > max_size_palindrome:
                max_size_palindrome = len(str1)
                palindrome = str1

    print(palindrome)
    return max_size_palindrome

str = "mollakayakokomassa"
print(longest_palindrome(str))
