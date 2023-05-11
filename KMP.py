def make_table(pattern):
    """
    Builds and returns the partial match table for a given pattern.
    Args: The pattern to build the table for.
    Returns: The partial match table for the pattern.
    """
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
    table = make_table(pattern)         # Build the partial match table for the pattern.
    m = 0
    i = 0
    while m + i < len(text):            # While the search window is inside the text:
        if pattern[i] == text[m + i]:   # If the current character matches the current pattern character
            i += 1                      # Increment the pattern index
            if i == len(pattern):       # If we've reached the end of the pattern
                result.append(m)        # Add the starting index of the match to the result
                m += 1                  # Increment the text index
                i = table[i-1]          # Shift the pattern index to the right
        else:
            m += i - table[i]           # Shift the text index to the right
            if i > 0:
                i = table[i]            # Shift the pattern index to the right
    return result
