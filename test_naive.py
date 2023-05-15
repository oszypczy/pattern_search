from naive import naive_search


def test_naive_search():
    text = "xyzabc123xyz0"
    pattern = "abc"
    result = naive_search(text, pattern)
    assert result == [3]


def test_naive_search_empty_text():
    text = ""
    pattern = "abc"
    result = naive_search(text, pattern)
    assert result == []


def test_naive_search_empty_pattern():
    text = "xyzabc123xyz0"
    pattern = ""
    result = naive_search(text, pattern)
    assert result == []


def test_naive_search_pattern_bigger_than_text():
    text = "xyzabc123xyz0"
    pattern = "abc123xyz0xyz"
    result = naive_search(text, pattern)
    assert result == []


def test_naive_serach_both_empty():
    text = ""
    pattern = ""
    result = naive_search(text, pattern)
    assert result == []


def test_naive_search_pattern_at_end():
    text = "xyzabc123xyz0"
    pattern = "0"
    result = naive_search(text, pattern)
    assert result == [12]


def test_naive_serach_pattern_equal_text():
    text = "xyzabc"
    pattern = "xyzabc"
    result = naive_search(text, pattern)
    assert result == [0]


def test_naive_search_pattern_not_in_text():
    text = "xyzabc"
    pattern = "123"
    result = naive_search(text, pattern)
    assert result == []


def test_naive_search_multiple_patterns():
    text = "xyzabc123xyz0"
    pattern = "xyz"
    result = naive_search(text, pattern)
    assert result == [0, 9]


def test_naive_search_long_text_2_letters_only():
    text = "abaaaabbbbbbbababbbbabbbaaaababbabaabbbabbbaab"
    pattern = "aba"
    result = naive_search(text, pattern)
    assert result == [0, 13, 27, 32]


def test_naive_search_long_text_3_letters_only():
    text = "ccccbbcbbcbcbabcbcbababbbbaacbbbacbbacba"
    pattern = "cba"
    result = naive_search(text, pattern)
    assert result == [11, 17, 37]
