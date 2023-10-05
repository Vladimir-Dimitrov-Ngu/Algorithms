# Assumption: we have massive with numbers <= M where M = 10^6 and a >= 0
from collections import defaultdict

M = 10 ^ 4
dict_numbers = {i: 0 for i in range(M)}


def digit_sort(a: list[int]) -> list[int]:
    global dict_numbers
    c = []
    for i in a:
        dict_numbers[i] += 1
    for key in dict_numbers:
        while dict_numbers[key] > 0:
            c.append(key)
            dict_numbers[key] -= 1
    return c


def test_digit_sort() -> None:
    assert digit_sort([0, 1, 2, 3]) == [0, 1, 2, 3], "Test 1"
    assert digit_sort([3, 2, 1, 0]) == [0, 1, 2, 3], "Test 2"
    assert digit_sort([0]) == [0], "Test 3"
    assert digit_sort([0, 10, 10, 10, 9, 8]) == [0, 8, 9, 10, 10, 10], "Test 4"
    assert digit_sort([]) == [], "Test 5"
    print("All test passed")


test_digit_sort()
