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
    s = 0
    for k in l:
        s = s + k
    return s


def find_element(l, a):
    """
    Find element a in list l and return index. Return -1 if it's not found in the list.
    """
    current_index = 0
    for c in l:
        if c == a:
            return current_index
        current_index = current_index + 1
    return -1


def find_min_idx_element(l):
    """
    Find index to the smallest value in the list
    """
    if l is None or len(l) == 0:
        return -1
    min_val = l[0]
    min_index = 0
    cur_idx = 0
    for cur_val in l:
        if cur_val < min_val:
            min_val = cur_val
            min_index = cur_idx
        cur_idx = cur_idx + 1

    return min_index


def reverse_list(l):
    """
    Returns a new list reversing the elements in the list l.
    """
    index = 0
    for m in l:
        index = index + 1
    j = index - 1
    new_list = []
    for k in l:
        new_list.append(l[j])
        j = j - 1
    return new_list


def concat_lists(l1, l2):
    """
    Concatenate lists l1 and l2 and return new list.
    """
    new_list = []
    for d in l1:
        new_list.append(d)
    for x in l2:
        new_list.append(x)
    return new_list


def tests():
    # Tests for sum_of_n()
    assert sum_of_n(1) == 1
    assert sum_of_n(-5) == 0
    assert sum_of_n(5) == 15
    print "All tests for sum_of_n() passed."

    # Tests for sum_of_list()
    assert sum_of_list([1, 5, 8]) == 14
    assert sum_of_list([]) == 0
    assert sum_of_list([100, 100, 100]) == 300
    assert sum_of_list([0, 0, 0]) == 0
    assert sum_of_list([-1, -1, -1]) == -3
    assert sum_of_list([10, 100, -1]) == 109
    assert sum_of_list([100]) == 100
    print "All tests for sum_of_list() passed."

    # Tests for find_element()
    assert find_element([4, 3, 8, 10], 8) == 2
    assert find_element([4, 3, 8, 10], 5) == -1
    assert find_element([1, 2, 10], 1) == 0
    assert find_element([1, 2, 3, 4, 5], 5) == 4
    assert find_element([1, 2, 3, 5], -1) == -1
    assert find_element([-2, -4, -6], 2) == -1
    assert find_element([0, 3, 0, 1], 0) == 0
    assert find_element([3, 3, 3, 3, 4], 3) == 0
    assert find_element([5, 3, 4, '%'], '%') == 3
    assert find_element([1, 2, 'hello'], 'hello') == 2
    print "All tests for find_element() passed"

    # Tests for min element index
    assert find_min_idx_element([1100, 1101, 1103, 1105, -1]) == 4
    assert find_min_idx_element([52, 42, 0, -4, -100]) == 4
    assert find_min_idx_element([0, 0, 0, 0]) == 0
    assert find_min_idx_element([100, -1000, -1000, -1]) == 1
    assert find_min_idx_element([]) == -1
    assert find_min_idx_element([1, 100000000000, -10000000000000000000000]) == 2
    assert find_min_idx_element(['h', 'i', 'a', 'A']) == 3
    assert find_min_idx_element(['hello', 'Hello']) == 1
    assert find_min_idx_element(['Hello', '123']) == 1
    print "All tests for find_min_idx_element() passed"

    # Tests for reverse_list()
    assert reverse_list([3, 5, 1]) == [1, 5, 3]
    assert reverse_list([]) == []
    assert reverse_list(['@', '&', '%']) == ['%', '&', '@']
    assert reverse_list(['hello']) == ['hello']
    print "All tests for reverse_list() passed"

    # Tests for concat_lists()
    assert concat_lists([3, 5, 1], [2, 3]) == [3, 5, 1, 2, 3]
    assert concat_lists([0, 1, 2, 3], [4, 5, 6]) == [0, 1, 2, 3, 4, 5, 6]
    assert concat_lists([0, 0], [0, 0]) == [0, 0, 0, 0]
    assert concat_lists([-1, 4, 7], [6, 3, 1]) == [-1, 4, 7, 6, 3, 1]
    assert concat_lists([], []) == []
    assert concat_lists(['s', 'app', 'hello', 3], [2, 3]) == ['s', 'app', 'hello', 3, 2, 3]
    assert concat_lists(['#', '$', '&'], ['!', '*']) == ['#', '$', '&', '!', '*']
    print "All tests for concat_lists() passed"

    return


if __name__ == "__main__":
    tests()
