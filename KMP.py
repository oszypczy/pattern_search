def make_table(pattern):
    """
    Builds and returns the partial match table for a given pattern.
    It says by what amount we can jump in the text if we fail to match a character in the pattern.
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
        if pattern[i - 1] == pattern[j]:    # looks for prefix/suffix match
            table[i] = j + 1                # if match, addjust table for correct jump
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
        return result                   # If the pattern is empty or bigger than the text, return an empty list.
    table = make_table(pattern)         # Build the partial match table for the pattern.
    m = 0                               # The index of the current character in the text.
    i = 0                               # The index of the current character in the pattern.
    while m + i < len(text):            # While the search window is inside the text:
        if pattern[i] == text[m + i]:   # If the current character matches the current pattern character
            i += 1                      # Increment the pattern index
            if i == len(pattern):       # If we've reached the end of the pattern
                result.append(m)        # Add the starting index of the match to the result
                m += 1                  # Increment the text index
                i = table[i-1]          # Shift the pattern index to the right
        else:
            m += i - table[i]           # if fails, jump in text by (current pos in pattern - value in table)
            if i > 0:
                i = table[i]            # Shift the pattern index to the right
    return result
