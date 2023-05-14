def naive_search(text, pattern):
    result = []
    pattern_bigger = True if len(pattern) > len(text) else False
    if len(pattern) == 0 or len(text) == 0 or pattern_bigger:
        return result                               # If the pattern is empty or bigger than the text, return an empty list.
    for i in range(len(text) - len(pattern) + 1):   # interate over every char in text looking for pattern
        if pattern == text[i: i + len(pattern)]:    # if pattern is found, add index to result
            result.append(i)
    return result
