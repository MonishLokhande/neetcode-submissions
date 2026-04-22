class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            k = nums.copy()
            i = nums.index(num)
            k.pop(i)
            if target - num in k:
                return [i, k.index(target-num)+1]