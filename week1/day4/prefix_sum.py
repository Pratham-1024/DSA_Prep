# Prefix sum template
nums = []
prefix = [0] * (len(nums) + 1)
for i in range(len(nums)):
    prefix[i+1] = prefix[i] + nums[i]

# sum of subarray [i..j] = prefix[j+1] - prefix[i]
# use a HashMap to store prefix sums seen so far
# for "subarray sum = k" → check if (current_sum - k) in seen