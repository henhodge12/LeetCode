class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        m, l, min, max, count = 0, 0, 0, 0, 0
        min_count, max_count = 0, 0
        for r in range(0, len(nums)):
            # if its out of bounds, reset our left window
            if nums[r] > maxK or nums[r] < minK:
                l = r + 1
            elif nums[r] >= max:
                max = nums[r]
                if max == maxK:
                    max_count += 1
            elif nums[r] < min:
                min = nums[r]
                if min == minK:
                    min_count += 1
            # check condition
            if max == maxK and min == minK:
                count += 1
                m = l
                while (True):
                    if nums[m] == max:
                        max_count -= 1
                    elif nums[m] == min:
                        min_count -= 1
                    m += 1
                    if max_count > 0 and min_count > 0:
                        count += 1
                    else:
                        break


        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
