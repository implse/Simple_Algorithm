# Base_62 Encoder / Decoder
BASE_ALPH = tuple("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
BASE_DICT = dict((c, v) for v, c in enumerate(BASE_ALPH))
BASE_LEN = len(BASE_ALPH)

# Base_62 Decoder
def base_decode(string):
    num = 0
    for char in string:
        num = num * BASE_LEN + BASE_DICT[char]
    return num

# Base_62 Decoder
def base_encode(num):
    if not num:
        return BASE_ALPH[0]
    encoding = ""
    while num > 0:
        num, remainder = divmod(num, BASE_LEN)
        encoding = BASE_ALPH[remainder] + encoding
    return encoding

d = base_decode("lazybrownfox")
print(d)
e = base_encode(d)
print(e)
