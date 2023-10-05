def merge(a: list[int], b: list[int]) -> list[int]:
    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


def merge_sort(a: list[int]) -> list[int]:
    if len(a) == 1 or len(a) == 0:
        return a
    half = len(a) // 2
    a_r = a[:half]
    a_l = a[half:]
    a_r = merge_sort(a_r)
    a_l = merge_sort(a_l)
    return merge(a_l, a_r)


def test_merge() -> None:
    assert merge([0, 1, 2], [3, 4, 5]) == [0, 1, 2, 3, 4, 5], "Test 1"
    assert merge([0, 2, 4], [1, 3, 5]) == [0, 1, 2, 3, 4, 5], "Test 2"
    assert merge([-5, -3, -2], [-6, -5, -4]) == [-6, -5, -5, -4, -3, -2], "Test 3"
    assert merge([0], [0]) == [0, 0], "Test 4"
    assert merge([], []) == [], "Test 5"


def test_merge_sort() -> None:
    assert merge_sort([0, 1, 2, 3]) == [0, 1, 2, 3], "Test 1"
    assert merge_sort([3, 2, 1, 0]) == [0, 1, 2, 3], "Test 2"
    assert merge_sort([0]) == [0], "Test 3"
    assert merge_sort([1, 2, -1, -2]) == [-2, -1, 1, 2], "Test 4"
    assert merge_sort([]) == [], "Test 5"
    print("All test passed")


test_merge()
test_merge_sort()
