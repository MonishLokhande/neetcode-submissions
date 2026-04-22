class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        old = {}
        for i, num in enumerate(nums):
            if target - num in old:
                return [old[target-num],i]
            old[num] = i