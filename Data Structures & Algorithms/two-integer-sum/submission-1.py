class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}

        for i in range(len(nums)):
            req = target - nums[i]
            if req in counter:
                return [counter[req], i]
            counter[nums[i]] = i
        return []