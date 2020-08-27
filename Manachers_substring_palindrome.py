# Manacher's Algorithm finds the longest palindrome substring in a string in O(n)

def UpdateString(string):
    newString = ["#"]
    for char in string:
        newString += ["#", char]
    return "".join(newString)


def Manacher(string):
    string = UpdateString(string)
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
print(Manacher(str))
