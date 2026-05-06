# Problem: Maximum Average Subarray I
# LeetCode: #643
# Difficulty: Easy
# Topic: Array / Sliding Window
# Pattern: Fixed size sliding window
# Time: O(n) | Space: O(1)
# Date: Day 3 of 90
# Status: Solved ✓ / revisit


from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg_sum = 0
        for avg in range(k):
            avg_sum += nums[avg]
        

        start = 1
        end = k
        max_avg = avg_sum / k

        while end < len(nums):
            avg_sum = avg_sum - nums[start-1]+ nums[end]
            curr_avg = avg_sum / k
            max_avg = max(max_avg,curr_avg)
            start += 1
            end += 1
        
        return max_avg
    
    # One pointer Approach (optimal)
        for i in range(k, len(nums)):
            avg_sum += nums[i] - nums[i - k]
            max_avg = max(max_avg, avg_sum / k)

        return max_avg
    

# Key insight: Instead of recomputing the sum of every k-length
# subarray from scratch (O(n*k)), slide a fixed window of size k.
# At each step, drop the leftmost element and add the new right one —
# the sum updates in O(1). Track the max average as you go.
# Fixed window size = simpler than variable window, one pointer enough.