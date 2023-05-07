def make_table(pattern):
    table = [0] * len(pattern)
    i = 2
    j = 0
    table[0] = -1
    if len(pattern) > 1:
        table[1] = 0
    while i < len(pattern):
        if pattern[i - 1] == pattern[j]:
            table[i] = j + 1
            i += 1
            j += 1
        else:
            if j > 0:
                j = table[j]
            else:
                table[i] = 0
                i += 1
    return table

def kmp_search(text, pattern):
    result = []
    pattern_bigger = True if len(pattern) > len(text) else False
    if len(pattern) == 0 or len(text) == 0 or pattern_bigger:
        return result
    table = make_table(pattern)
    m = 0
    i = 0
    while m + i < len(text):
        if pattern[i] == text[m + i]:
            i += 1
            if i == len(pattern):
                result.append(m)
                m += 1
                i = table[i-1]
        else:
            m += i - table[i]
            if i > 0:
                i = table[i]
    return result
