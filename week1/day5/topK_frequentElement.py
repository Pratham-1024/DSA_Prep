# Problem: Top K Frequent Elements
# LeetCode: #347
# Difficulty: Medium
# Topic: HashMap / Heap / Sorting
# Pattern: HashMap + Sorting / Heap / Bucket Sort
# Time: O(n log n) | Space: O(n)  ← your current solution
# Date: Day 5 of 90
# Status: Solved ✓ / resolve


from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
    
        # Optimization-1
        import heapq
        return heapq.nlargest(k, count.keys(), key=count.get)
    
        # Optimization-2
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


    
# Key insight: Count frequencies with a HashMap, then retrieve
# the top k by frequency. Sorting the frequency array works but
# costs O(n log n). A heap of size k brings it to O(n log k).
# Optimal: bucket sort — index each bucket by frequency (max = n),
# then scan buckets from high to low. Guaranteed O(n) since
# frequency is bounded by array length, no comparison sort needed.
