def is_pangram(sent):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lstr = list(sent.replace(" ","").lower())
    for a in alphabet:
        if a in lstr:
            True
        else:
           return False
    return True

is_pangram('"Five quacking Zephyrs jolt my wax bed."')