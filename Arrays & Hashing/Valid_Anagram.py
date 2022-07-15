class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        let= set(s)
        for x in let:
            if s.count(x)!= t.count(x): return False
        return True