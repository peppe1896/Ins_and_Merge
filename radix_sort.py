def counting_sort(array, place, size):
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


def radix_sort(array):
    max_element = max(array)
    place = 1
    size = len(array)
    while max_element // place > 0:
        counting_sort(array, place, size)
        place *= 10
