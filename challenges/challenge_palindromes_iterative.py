def is_palindrome_iterative(word):
    if word == '':
        return False
    low_index = 0
    high_index = len(word) - 1
    result = True
    while high_index != low_index and high_index > low_index:
        if word[high_index] != word[low_index]:
            result = False
            break
        low_index += 1
        high_index -= 1
    return result
