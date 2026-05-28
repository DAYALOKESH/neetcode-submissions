class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        for char in strs:
            counter["".join(sorted(char))].append(char)

        return list(counter.values())