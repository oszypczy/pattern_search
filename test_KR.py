from KR import KRsearch
# pusty jeden lub oba napisy wejściowe,
# napisstringrówny napisowitext
# napisstringdłuższy od napisutext
# napisstringnie występuje wtext.
def test_kmp_search():
    text = "xyzabc123xyz0"
    pattern = "abc"
    result = KRsearch(text, pattern)
    assert result == [3]

def test_kmp_search_empty_text():
    text = ""
    pattern = "abc"
    result = KRsearch(text, pattern)
    assert result == []

def test_kmp_search_empty_pattern():
    text = "xyzabc123xyz0"
    pattern = ""
    result = KRsearch(text, pattern)
    assert result == []

def test_kmp_search_pattern_bigger_than_text():
    text = "xyzabc123xyz0"
    pattern = "xyzabc123xyz0AAAAAAA"
    result = KRsearch(text, pattern)
    assert result == []

def test_kmp_serach_both_empty():
    text = ""
    pattern = ""
    result = KRsearch(text, pattern)
    assert result == []

def test_kmp_search_pattern_at_end():
    text = "xyzabc123xyz0"
    pattern = "0"
    result = KRsearch(text, pattern)
    assert result == [12]

def test_kmp_serach_pattern_equal_text():
    text = "xyzabc"
    pattern = "xyzabc"
    result = KRsearch(text, pattern)
    assert result == [0]

def test_kmp_search_pattern_not_in_text():
    text = "xyzabc"
    pattern = "123"
    result = KRsearch(text, pattern)
    assert result == []

def test_kmp_search_multiple_patterns():
    text = "xyzabc123xyz0"
    pattern = "xyz"
    result = KRsearch(text, pattern)
    assert result == [0, 9]

def test_kmp_search_long_text_2_letters_only():
    text = "abaaaabbbbbbbababbbbabbbaaaababbabaabbbabbbaab"
    pattern = "aba"
    result = KRsearch(text, pattern)
    assert result == [0, 13, 27, 32]
