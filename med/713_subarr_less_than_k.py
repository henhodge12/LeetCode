class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        totalscore = 0
        totalarray = 0
        for i in range(0, len(nums)):
            totalscore = nums[i]
            if totalscore < k:
                totalarray += 1
            else:
                continue
            for j in range(i+1, len(nums)):
                totalscore += nums[j]
                if totalscore >= k:
                    break
                else:
                    totalarray += 1
        return totalscore

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

