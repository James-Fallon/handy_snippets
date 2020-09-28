import logging
logging.basicConfig(level=logging.INFO)


def _partition(array, left, right, pivot):

    while left <= right:
        while array[left] < pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if left <= right:
            left_val = array[left]
            array[left] = array[right]
            array[right] = left_val
            left += 1
            right -= 1

    return left


def _quick_sort(array, left, right):
    if left >= right:
        return

    pivot = array[(left + right) // 2]
    partition_index = _partition(array, left, right, pivot)
    _quick_sort(array, left, partition_index - 1)
    _quick_sort(array, partition_index, right)

    return array


def quick_sort(array):
    return _quick_sort(array, 0, len(array) - 1)


if __name__ == '__main__':

    integers = [23423, 32, 23, 4, 2342, 42357, 68, 45634532, 7, 478356724, 6354, 5746, 3]
    logging.info(quick_sort(integers))


