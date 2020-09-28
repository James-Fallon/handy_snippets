

def binary_search(array, x):

    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == x:
            return True
        elif x < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False


if __name__ == '__main__':

    integers = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13]
    print(binary_search(integers, 7))
    print(binary_search(integers, 1))
    print(binary_search(integers, 13))
    print(binary_search(integers, 6))
    print(binary_search(integers, 11))
