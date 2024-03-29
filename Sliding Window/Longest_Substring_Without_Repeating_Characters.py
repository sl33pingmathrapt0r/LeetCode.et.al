class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start= end= 0
        length= 0
        seen= {}
        while end < len(s):
            if s[end] in seen:
                while seen[s[end]] and seen[s[end]][0] < start: seen[s[end]].pop(0)
                if seen[s[end]] == []: 
                    seen[s[end]].append(end)
                else:
                    length= length if length > (end-start) else end - start
                    start= seen[s[end]].pop(0) + 1
                    seen[s[end]].append(end)
            else: 
                seen[s[end]]= [end]
            end+= 1
        length= length if length > (end-start) else end - start
        return length
