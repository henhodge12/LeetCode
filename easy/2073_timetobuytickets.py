# 4/9/2024
# tickets is a list of length n
# it represents a line of people waiting to buy a ticket
# each ticket takes 1 second to buy
# tickets[i] = the amount of tickets the ith customer wants to purchase
# calculate how many seconds it takes for customer 'k' to purchase their
# desired amount of tickets
# this can be solved with your eyes closed in O(n^2)
# if we think about the array before and after the index we want, we can cut
# that to O(n) with ease
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        sec = tickets[k]
        for i in range(0, len(tickets)):
            if i == k:
                continue
            elif i < k:
                if (tickets[i] <= tickets[k]):
                    sec += tickets[i]
                else:
                    sec += tickets[k]
            else:
                if tickets[i] < tickets[k]:
                    sec += tickets[i]
                else:
                    sec += tickets[k] - 1
        return sec
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
