class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in table:
                return [table[num], i]
            table[nums[i]] = i