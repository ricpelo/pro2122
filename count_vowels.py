def count_vowels(txt):
    if txt == '':
        return 0
    if txt[0].lower() in 'aeiou':
        res = 1
    else:
        res = 0
    return res + count_vowels(txt[1:])
