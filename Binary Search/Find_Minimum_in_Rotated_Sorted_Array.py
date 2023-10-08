class Solution(object):
    """
    A sorted array (in ascending order) is
    Left-rotated some number of indexes.
    E.g. [4,5,6,7,0,1,2,3] was rotated 4 indexes.

    Find the minimum element of the array.
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]

        if nums[0]<nums[-1]:
            return nums[0]

        if len(nums)==2:
            return nums[-1]

        n= len(nums)
        cur= n//2
        if nums[cur] < nums[cur-1] and nums[cur] < nums [cur+1]:
            return nums[cur]

        if nums[0]<nums[cur]:
            return findMin(self, nums[cur+1:])
        else:
            return findMin(self, nums[:cur])
