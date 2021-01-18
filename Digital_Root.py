# We're provided a positive integer num.
# Can you write a method to repeatedly sum all of its digits until the result has only one digit?
# The digital root of a positive integer is found by summing the digits of the integer.

import math

def digitalRoot(num):

    if num == "0":
        return 0

    digits_sum = 0

    for i in range (0, len(num)):
        digits_sum = (digits_sum + int(num[i])) % 9

    if digits_sum == 0:
        return 9
    else:
        return digits_sum % 9


print(digitalRoot(str(49)))
