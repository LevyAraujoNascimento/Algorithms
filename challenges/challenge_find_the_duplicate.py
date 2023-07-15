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


def test(num):
    if num < 0:
        return True
    elif isinstance(num, str):
        return True
    else:
        return False


def find_duplicate(nums):
    if len(nums) <= 1 or isinstance(nums[0], str):
        return False
    count = 1
    result = False
    quick_sort(nums, 0, len(nums) - 1)
    while count <= len(nums) - 1:
        if test(nums[count]) or test(nums[count - 1]):
            break
        elif nums[count] == nums[count - 1]:
            result = nums[count]
            break
        else:
            count += 1
    return result
