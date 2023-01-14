# Time complexity: O(n) - sum is O(n) and we have a while loop with at most n iterations
# Space complexity:O(1) - we always store 3 ints

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums[1:])
        i = 0
        if left_sum == right_sum:
            return i
        while i < len(nums)-1:
            i += 1
            left_sum += nums[i-1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
        return -1