def sum_of_n(n):
    """
    Sum of all numbers until n.
    """
    if n < 1:
        return 0

    s = 0
    for i in range(1, n + 1):
        s += i
    return s


def sum_of_list(l):
    """
    Sum of all numbers in list l.
    """
    return 0


def find_element(l, a):
    """
    Find element a in list l and return index. Return -1 if it's not found in the list.
    """
    return -1


def sort_list(l):
    """
    Sort integers in list l.
    """
    return l


def reverse_list(l):
    """
    Returns a new list reversing the elements in the list l.
    """
    return l


def concat_lists(l1, l2):
    """
    Concatenate lists l1 and l2 and return new list.
    """
    return []


def merge_lists(l1, l2):
    """
    l1 and l2 are always sorted and unique elements(no duplicates).
    Return a new list that merges l1 and l2 in sorted order and remove any duplicates.
    """
    return []


def tests():
    # Tests for sum_of_n()
    assert sum_of_n(1) == 1
    assert sum_of_n(-5) == 0
    assert sum_of_n(5) == 15
    print "All tests for sum_of_n() passed."

    return

    # Tests for sum_of_list()
    assert sum_of_list([1, 5, 8]) == 14
    assert sum_of_list([]) == 0
    # TODO: Write more test cases
    print "All tests for sum_of_list() passed."

    # Tests for find_element()
    assert find_element([4, 3, 8, 10], 8) == 2
    assert find_element([4, 3, 8, 10], 5) == -1
    # TODO: Write more test cases
    print "All tests for find_element() passed"

    # Tests for sort_list()
    assert sort_list([3, 5, 1]) == [1, 3, 5]
    # TODO: Write more test cases
    print "All tests for sort_list() passed"

    # Tests for reverse_list()
    assert reverse_list([3, 5, 1]) == [1, 5, 3]
    # TODO: Write more test cases
    print "All tests for reverse_list() passed"

    # Tests for concat_lists()
    assert concat_lists([3, 5, 1], [2, 3]) == [3, 5, 1, 2, 3]
    # TODO: Write more test cases
    print "All tests for concat_lists() passed"

    # Tests for merge_lists()
    assert merge_lists([1, 3, 5], [4, 8]) == [1, 3, 4, 5, 8]
    # TODO: Write more test cases
    print "All tests for merge_lists() passed"


if __name__ == "__main__":
    tests()