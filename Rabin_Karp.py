# The Rabin-Karp algorithm is a string-searching algorithm that uses hashing to find patterns in strings.


class RollingHash:
    def __init__(self, text, sizeWord):
        self.text = text
        self.hash = 0
        self.sizeWord = sizeWord

        for i in range(0, sizeWord):
            self.hash += (ord(self.text[i]) - ord("a")+1)*(26**(sizeWord - i -1))

        self.window_start = 0
        self.window_end = sizeWord

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            self.hash -= (ord(self.text[self.window_start]) - ord("a")+1)*26**(self.sizeWord-1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end])- ord("a")+1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]

def rabin_karp(s, x):
    if s == "" or x == "":
        return None
    if len(s) > len(x):
        return None

    rolling_hash = RollingHash(x, len(s))
    s_hash = RollingHash(s, len(s))

    for i in range(len(x) - len(s) + 1):
        if rolling_hash.hash == s_hash.hash:
            if rolling_hash.window_text() == s:
                return i
        rolling_hash.move_window()
    return None
