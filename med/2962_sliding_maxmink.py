# 3/29/24
# find the number of subarrays containing the max element at least k times

class Solution(object):
    def countSubarrays(self, nums, k):
        max_val = max(nums)
        r, l, count, sa = 0, 0, 0, 0
        n = len(nums)
        # sliding window
        while r < n:
            if nums[r] != max_val:
                r += 1
                continue
            else:
                count += 1
                if count < k:
                    r += 1
                    continue
                else:
                    # n -r counts all subarrays containing at least k max's
                    sa += n-r
                    while nums[l] != max_val:
                        l += 1
                        # this increments l and counts all new subarrays
                        sa += n-r
                    l += 1
                    count -= 1
                    r += 1
        return sa
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
