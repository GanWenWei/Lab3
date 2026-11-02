import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)



def test_bubble_sort_equal_above_10():
    input_arr = [64, 34, 25, 12, 22, 11, 90,15,22,84,69]
    assert Lab3.bubble_sort(input_arr,Lab3.SORT_DESCENDING) == 1

def test_bubble_sort_equal_0():
    input_arr = []
    assert Lab3.bubble_sort(input_arr,Lab3.SORT_DESCENDING) == 0

def test_bubble_sort_equal_is_not_integer():
    input_arr = [1,2,"abc",4]
    assert Lab3.bubble_sort(input_arr,Lab3.SORT_DESCENDING) == 2
