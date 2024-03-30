# 3/29/24
# first hard problem
# uses sliding windown to find total subarrays with k distinct integers
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        sa_count, l, r, count, n = 0, 0, 0, 0, len(nums)
        ltmp = 0
        box = [0] * (n+1)
        # main loop
        while r < n:
            # checking if next integer is distinct
            if box[nums[r]] == 0:
                count += 1
            box[nums[r]] += 1
            # if count > k, increment left pane to make windown smaller
            if count > k:
                box[nums[l]] -= 1
                while box[nums[l]] != 0:
                    print(box[nums[l]])
                    l += 1
                    box[nums[l]] -= 1
                count -= 1
                l += 1
            # if count == k, add to subarray count
            if count == k:
                sa_count += 1
                ltmp = l
                # this section counts all subarrays from l - r
                if ltmp == r:
                    r += 1
                    continue
                while ltmp <= r:
                    box[nums[ltmp]] -= 1
                    if box[nums[ltmp]] == 0:
                        break
                    else:
                        sa_count += 1
                        ltmp += 1
                while ltmp >= l:
                    box[nums[ltmp]] += 1
                    ltmp -= 1

            r += 1
        return sa_count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

