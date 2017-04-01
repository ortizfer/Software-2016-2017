

# Functions take a string, and adds as many characters as needed to reach
# the specified length, position determines if it is added before or after
# the string: positions larger than 0 concatenate the characters after the
# string; positions equal or smaller than 0 concatenates the characters
# before the string.

def extendString(string, character, length, position):
    amount = length - len(string)
    extension = ""
    while len(extension) < amount:
        extension = extension + character

    if position > 0:
        nstr = string + extension
    else:
        nstr = extension + string

    return nstr



'''
VERSION CONTROL:

1- Carlos J. Figueroa 01/04/2017 2:47pm
Initial File creation. Added function extendString.
'''