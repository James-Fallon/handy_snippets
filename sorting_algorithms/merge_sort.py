import logging
logging.basicConfig(level=logging.INFO)


def _merge_halves(left, right):
    result = []

    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result


def merge_sort(array):

    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return _merge_halves(left, right)


if __name__ == '__main__':

    integers = [23423, 32, 23, 4, 2342, 42357, 68, 45634532, 7, 478356724, 6354, 5746, 3]
    logging.info(merge_sort(integers))
