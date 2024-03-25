# 3/25/2024
# Each number occurs either once or twice in the array. Return all duplicates.
class Solution(object):
    def findDuplicates(self, nums):
        new_nums = [0] * (len(nums) + 1)
        dupes = []
        
        for num in nums:
            if (new_nums[num] == 0):
                new_nums[num] = 1
            elif (new_nums[num] == 1):
                dupes.append(num)
            
        return dupes
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        