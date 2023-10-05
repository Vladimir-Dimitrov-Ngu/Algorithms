def bubble(a: list[int]) -> list[int]:
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a


def test() -> None:
    assert bubble([0, 1, 2, 3]) == [0, 1, 2, 3], 'Test 1'
    assert bubble([3, 2, 1, 0]) == [0, 1, 2, 3], 'Test 2'
    assert bubble([0]) == [0], 'Test 3'
    assert bubble([1, 2, -1, -2]) == [-2, -1, 1, 2], 'Test 4'
    assert bubble([]) == [], 'Test 5'
    print("All test passed")


test()
