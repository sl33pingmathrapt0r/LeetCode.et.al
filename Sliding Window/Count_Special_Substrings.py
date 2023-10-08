"""
Given a string containing digits
only 0-9, and a special number k,
find the number of special
substrings. Every character in the
special substring appears k times.

Eg. 1102022, k=2
    4 special substrings:
    11
    110202
    0202
    22
"""
def special_substrings(s: str, k: int) -> int:
    """
    implementing sliding window
    """
    chars= {}
    start= end= count= 0
    valid= set([k])

    while end < len(s):
        chars[s[end]]= chars.get(s[end], 0)+1
        while chars[s[end]] > k:
            chars[s[start]] -= 1
            if chars[s[start]] == 0:
                chars.pop(s[start])
            start+=1

        end += 1

        counts= set(chars.values())
        if counts==valid:
            count+=1

        if k in counts:
            charcopy= dict(zip(chars.keys(), chars.values()))
            iterate= start
            while k in charcopy.values():
                charcopy[s[iterate]] -= 1
                if charcopy[s[iterate]] == 0:
                    charcopy.pop(s[iterate])
                iterate+=1
                if set(charcopy.values())==valid:
                    count+=1

    return count
