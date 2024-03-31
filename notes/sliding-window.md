# Sliding Window Tehcnique
### The Sliding Window Technique is used when we need to find subarrays that meet a condition.
### The idea behind this technique is to maintain a left side of the window and right side of the window that we increment in order to check conditions in our main array.
### The benefit of this technique is that we can bring time complexity from O(n^2) (nested loops) to O(n).
### In order to solve these problems, we can tweak the algorithm below to find the answer.
- Iterate right side of window until condition is true
- If condition is false, iterate left side of window until it is true again
- Repeat this process until we reach the end of the array  
Some example cases include:  
- finding the max sum for a contiguos subarray of length k
- finding all subarrays with max k and min K
- finding all subarrays of sum k  
Example LeetCode Problems:  

