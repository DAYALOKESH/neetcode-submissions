class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        res = []

        for num, cnt in counter.items():
            res.append([num, cnt])
        
        sorted_list = sorted(res, key = lambda item: item[1], reverse = True)
        for i in range(len(sorted_list)):
            sorted_list[i] = sorted_list[i][0]
        return sorted_list[:k]
