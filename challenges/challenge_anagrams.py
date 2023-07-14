def quick_sort(array, start, end):
    if start < end:
        p = partition(array, start, end)
        quick_sort(array, start, p - 1)
        quick_sort(array, p + 1, end)


def partition(array, start, end):
    pivot = array[end]
    delimiter = start - 1
    for i in range(start, end):
        if array[i] <= pivot:
            delimiter = delimiter + 1
            array[i], array[delimiter] = array[delimiter], array[i]
    array[delimiter + 1], array[end] = array[end], array[delimiter + 1]
    return delimiter + 1


def is_anagram(first_string, second_string):
    strA = list(first_string.lower())
    strB = list(second_string.lower())
    quick_sort(strA, 0, len(strA) - 1)
    quick_sort(strB, 0, len(strB) - 1)
    if first_string == '' and second_string == '':
        return ('', '', False)
    else:
        return (''.join(strA), ''.join(strB), strA == strB)


x = 'Levy'
y = 'yvel'
print(is_anagram(x, y))
