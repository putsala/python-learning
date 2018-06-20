def multi_list(l):
    """Given a list and multiply each and every element with 2"""
    output_list = []
    for i in l:
        output_list.append(i * 2)
    return output_list


def new_list(l):
    """Given a list and multiply each and every element with 2"""
    o = [x * 2 for x in l]
    return o


def string_times(string, n):
    """Given a string and a non-negative int n, return a larger string that is n copies of the original string"""
    sum_of = ''
    for i in range(0, n):
        sum_of = sum_of + string
    return sum_of


def not_string(string):
    """Given a string, return a new string where "not " has been added to the front. However,
    if the string already begins with "not", return the string unchanged."""
    if len(string) >= 3 and (string[0] == 'n' and string[1] == 'o' and string[2] == 't'):
        return string
    else:
        return 'not ' + string


def front_back(string):
    """* Given a string, return a new string where the first and last chars have been exchanged
    """
    if len(string) <= 1:
        return string
    start = string[len(string) - 1]
    mid = string[1: len(string) - 1]
    str1 = start + mid + string[0]
    return str1


def front3(s):
    """Given a string, we'll say that the front is the first 3 chars of the string.
     If the string length is less than 3, the front is whatever is there.
     Return a new string which is 3 copies of the front"""
    length = len(s) if len(s) < 3 else 3
    return s[0: length] * 3


def front_times(s, n):
    """Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
    or whatever is there if the string is less than length 3. Return n copies of the front"""
    length = len(s) if len(s) < 3 else 3
    return s[:length] * n


def tests():
    # Tests for string_times
    assert string_times('hello', 2) == 'hellohello'
    assert string_times('', 0) == ''
    assert string_times('hello', 0) == ''
    assert string_times('h', -3) == ''
    assert string_times('h', 10) == 'hhhhhhhhhh'
    assert string_times('2', 2) == '22'
    assert string_times('@#$%', 1) == '@#$%'

    # Tests for not_string
    assert not_string('not there') == 'not there'
    assert not_string('hello there') == 'not hello there'
    assert not_string('hello not there') == 'not hello not there'
    assert not_string('@#$%^&') == 'not @#$%^&'
    assert not_string('1234567') == 'not 1234567'
    assert not_string("12345") == "not 12345"
    assert not_string('a') == 'not a'

    # Tests for front_back
    assert front_back('code') == 'eodc'
    assert front_back('h') == 'h'
    assert front_back('12345') == '52341'
    assert front_back('-1-2-3') == '31-2--'
    assert front_back('') == ''
    assert front_back('hi') == 'ih'

    # Tests for front3
    assert front3('h') == 'hhh'
    assert front3('h1') == 'h1h1h1'
    assert front3('coc') == 'coccoccoc'
    assert front3('') == ''
    assert front3('World is going very fast and polluting so much because of people in it') == 'WorWorWor'
    assert front3('12345') == '123123123'
    assert front3('-1-10-20') == '-1--1--1-'

    # Tests for front_times
    assert front_times('abc', 2) == 'abcabc'
    assert front_times('', 0) == ''
    assert front_times('abc', -1) == ''
    assert front_times('a', 3) == 'aaa'
    assert front_times('123', 3) == '123123123'
    assert front_times('a', 10) == 'aaaaaaaaaa'
    assert front_times('hello there how are you mate', 1) == 'hel'
    assert front_times('hello there how are you mate', 0) == ''

    # Test for multi_list
    assert multi_list([1, 2, 3, 4]) == [2, 4, 6, 8]
    assert multi_list([]) == []
    assert multi_list(['hello', 'there', 2, 4]) == ['hellohello', 'therethere', 4, 8]
    assert multi_list([-1, -10, -20]) == [-2, -20, -40]
    assert multi_list([2.2, -3.0, 550.2]) == [4.4, -6.0, 1100.4]
    assert multi_list([0]) == [0]

    # Test for new_list
    assert new_list([1, 2, 3, 4]) == [2, 4, 6, 8]
    assert new_list([]) == []
    assert new_list(['hello', 'there', 2, 4]) == ['hellohello', 'therethere', 4, 8]
    assert new_list([-1, -10, -20]) == [-2, -20, -40]
    assert new_list([2.2, -3.0, 550.2]) == [4.4, -6.0, 1100.4]
    assert new_list([0]) == [0]

    return


if __name__ == "__main__":
    tests()
