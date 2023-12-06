# RAW APPROACH: checking wordlist against string
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        true_cache = set()
        false_cache = set()

        def helper(s, wordDict):
            if s in true_cache:
                return True
            elif s in false_cache:
                return False

            if s in wordDict or not s:
                true_cache.add(s)
                return True

            i=0
            while i < len(wordDict):
                if wordDict[i] not in s:
                    wordDict.pop(i)
                else:
                    i+=1

            if not wordDict:
                false_cache.add(s)
                return False

            for word in wordDict:
                wordLoc = s.find(word)
                before, after = s[:wordLoc], s[wordLoc+len(word):]
                newDict= [word for word in wordDict]
                temp = helper(before, newDict) and helper(after, newDict)
                if temp:
                    true_cache.add(s)
                    return True
                else:
                    false_cache.add(s)

            return False

        return helper(s, wordDict)


# BETTER APPROACH: checking string against wordlist
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n= len(s)
        wordDict = set(wordDict)
        cache = [False]*(n+1)
        cache[0] = True

        for i in range(1,n+1):
            for j in range(i):
                if cache[j] and s[j:i] in wordDict:
                    cache[i] = True
                    break

        return cache[n]
