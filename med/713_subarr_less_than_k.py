# 3/26/2024
# i had to look at the solution for this because mine was too slow
# it uses the 'sliding window' technique, where we increment the left
# and right indices with each iteration, constaining our time complexity to O(n)
# i used nested for loops first which is clearly O(n^2)
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        product = 1
        r = 0
        l = 0
        total = 0
        if k <= 1:
            return 0
        while r < len(nums):
            product *= nums[r]
            while product >= k:
                product /= nums[l]
                l += 1
            total += 1 + (r - l)
            r += 1
        return total
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
