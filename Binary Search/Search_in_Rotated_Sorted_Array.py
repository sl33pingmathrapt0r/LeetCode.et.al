class Solution(object):
    """
    A sorted (ascending) array is left-rotated
    some number of places.
    E.g. [4,5,6,7,0,1,2,3] was rotated 4 places.
    (equivalent to pivot at index 4)
    Given the mutated array and some target,
    return the index of the target, or -1 if
    the target is not in the array.
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n= len(nums)

        if n==0:
            return -1

        if n==1:
            return 0 if nums[0]==target else -1

        lower=0
        upper=n-1
        cur= n//2

        while lower<upper:
            if nums[cur]==target:
                return cur

            if nums[lower] <= target < nums[cur]:
                upper= cur
                cur= (lower+upper)//2
            elif nums[lower] < nums[cur]:
                lower= cur
                cur= (lower+upper)//2 +1
            elif nums[lower] <= target or target < nums[cur]:
                upper= cur
                cur= (lower+upper)//2
            else:
                lower= cur
                cur= (lower+upper)//2 +1

        if nums[lower]==target:
            return lower
        else:
            return -1
