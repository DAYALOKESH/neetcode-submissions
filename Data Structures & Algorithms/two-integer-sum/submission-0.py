class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in counter.keys():
                return [counter[needed], i]
            counter[nums[i]] = i
        return []