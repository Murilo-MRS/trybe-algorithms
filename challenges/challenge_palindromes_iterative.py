def is_palindrome_iterative(word):
    # baseado em
    # https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
    if len(word) == 0:
        return False
    for index in range(0, int(len(word) / 2)):
        if word[index] != word[len(word) - index - 1]:
            return False
    return True
