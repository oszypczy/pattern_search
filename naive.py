def naive_search(text, pattern):
    result = []
    pattern_bigger = True if len(pattern) > len(text) else False
    if len(pattern) == 0 or len(text) == 0 or pattern_bigger:
        return result
    for i in range(len(text) - len(pattern) + 1):
        if pattern == text[i: i + len(pattern)]:
            result.append(i)
    return result
