# 1480. Running Sum of 1d Array
[Running Sum of 1d Array - LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/description/?envType=study-plan&id=level-1)

This is a very simple problem so the solution is basically the same in every language.
Here is the solution in Python. We have to go once through the array so it's O(n) in time, and O(1) in space if we just edit original list in-place.

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
```

- You can also use accumulate from itertools but that's probably too cheeky
```python
from itertools import accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)
```