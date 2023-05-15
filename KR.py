def KRsearch(text, pattern, q=(2**60)-243):
    m = len(pattern) # pattern length
    n = len(text) # text length
    d = 10 # optional to chose ?
    #q = len(set(text))
    p = 0 # hash for pattern
    t = 0 # hash for text
    h = 1
    results = []
    if(m>n):
        return []
    if (n>0 and m>0):
        for i in range(m-1): # takjakby text hash -> sluzy do usuwania udzialu hashu przy przesuwaniu
            h = (h*d) % q # d^(m-1)

        # Calculate hash value for pattern and text
        for i in range(m):
            p = (d*p + ord(pattern[i])) % q # pattern hash - permament
            t = (d*t + ord(text[i])) % q    # text hash

        # Find the match
        for i in range(n-m+1): # iterate for each 3 letters
            if p == t: # character-matching condition
                for j in range(m): # checking if letters are the same
                    if text[i+j] != pattern[j]:
                        break
                # bo jesli kazda litera jest taka sama to podkoniec 'j' bedzie = (m-1)
                j += 1 # check if end of pattern was reached
                if j == m: # if so -> append
                    results.append(i)

            if i < n-m: # == if not last iteration
                t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q # update text hash as we move the substrng
        # usuwa udzial poprzedniego hasha    # ^kolejna litera
                if t < 0:
                    t = t+q
    return results