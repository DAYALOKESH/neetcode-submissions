class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i, num in enumerate(nums):
            req = target - num
            if req in count:
                return [count[req], i]
            count[num] = i
        return False
