class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        n = len(candidates)
        result, cache= [], []
        for candidate in candidates:
            if candidate == target:
                result.append([candidate])
            elif candidate < target:
                cache.append([candidate])

        # implement BFS with unique tree path
        while cache:
            ls = cache.pop(0)
            cur = sum(ls)
            # ensure unique path
            subindex = candidates.index(ls[-1])
            for i in range(subindex,n):
                if candidates[i] == target-cur:
                    result.append(ls + [candidates[i]])
                elif candidates[i] < target - cur:
                    cache.append(ls+[candidates[i]])

        return result
