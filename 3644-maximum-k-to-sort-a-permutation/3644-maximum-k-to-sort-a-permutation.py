from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        if all(nums[i] == i for i in range(n)):
            return 0

        result = (1 << max(1, (n - 1).bit_length())) - 1
        for i, num in enumerate(nums):
            if num != i:
                result &= (i & num)
        return result