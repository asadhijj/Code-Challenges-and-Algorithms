def repeated_word(string):
    list = string.split()
    hash=set()
    for word in list:
        if word in hash:
            return word
        else :
            hash.add(word)
    return "No Repetition"