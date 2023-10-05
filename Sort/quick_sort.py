from random import randint


def quick_sort(array: list[int], left: int, right: int) -> None:
    if left < right:
        i, j = left, right
        middle = array[randint(left, right)]

        while i <= j:
            while array[i] < middle:
                i += 1
            while array[j] > middle:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        quick_sort(array, left, j)
        quick_sort(array, i, right)
    return array


def test_quick_sort() -> None:
    assert quick_sort([0, 1, 2, 3], 0, 3) == [0, 1, 2, 3], "Test 1"
    assert quick_sort([3, 2, 1, 0], 0, 3) == [0, 1, 2, 3], "Test 2"
    assert quick_sort([0], 0, 0) == [0], "Test 3"
    assert quick_sort([1, 2, -1, -2], 0, 3) == [-2, -1, 1, 2], "Test 4"
    assert quick_sort([], 0, 0) == [], "Test 5"
    print("All test passed")


test_quick_sort()
