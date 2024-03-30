class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        sa_count, l, r, count, n = 0, 0, 0, 0, len(nums)
        ltmp = 0
        box = [0] * (n+1)
        while r < n:
            if box[nums[r]] == 0:
                count += 1
            box[nums[r]] += 1
            if count > k:
                box[nums[l]] -= 1
                while box[nums[l]] != 0:
                    l += 1
                    box[nums[l]] -= 1
                count -= 1
                l += 1
            if count == k:
                sa_count += 1
                ltmp = l
                while ltmp < r:
                    box[nums[ltmp]] -= 1
                    if box[nums[ltmp]] == 0:
                        break
                    else:
                        sa_count += 1
                        ltmp += 1
                while ltmp >= l:
                    print(ltmp)
                    box[nums[ltmp]] += 1
                    ltmp -= 1
            r += 1
        return sa_count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
