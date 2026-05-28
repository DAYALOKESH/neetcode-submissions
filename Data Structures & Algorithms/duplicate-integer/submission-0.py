class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}

        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
            if counter[nums[i]] != 1:
                return True
        return False