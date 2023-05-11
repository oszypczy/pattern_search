def KRsearch(text, pattern):
    """This implementation uses the ASCII values of the characters in the pattern and text strings
    to calculate their hash values, and then compares these hash values to determine if there is
    a match between the pattern and a substring of the text.
    The power_mod list is used to efficiently compute the hash values for each substring,
    and the p and m constants are used to reduce the likelihood of hash collisions."""
    if len(pattern) == 0 or len(text) < len(pattern):
        return []
    p = 31
    m = 10**9 + 9
    n = len(text)
    k = len(pattern)
    power_mod = [1] * (n-k+1)
    for i in range(1, n-k+1):
        power_mod[i] = (power_mod[i-1]*p) % m
    hash_pattern = 0
    hash_text = 0
    for i in range(k):
        hash_pattern = (hash_pattern*p + ord(pattern[i])) % m
        hash_text = (hash_text*p + ord(text[i])) % m
    indexes = []
    for i in range(n-k+1):
        if hash_pattern == hash_text:
            if text[i:i+k] == pattern:
                indexes.append(i)
        if i < n-k:
            hash_text = ((hash_text - ord(text[i])*power_mod[k-1])*p + ord(text[i+k])) % m # noqa 551
            hash_text = (hash_text + m) % m
    return indexes