class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        left = 0
        res = []

        for left in range(n):
            right = left + 1
            count = 1
            while right < n:
                if temperatures[right] > temperatures[left]:
                    break
                right += 1
                count +=1
            count = 0 if right == n else count
            res.append(count)
        return res

