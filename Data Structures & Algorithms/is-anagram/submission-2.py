
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length doesnt match no point saying they are identical
        if len(s) != len(t):
            return False
        # declaring the counter dictionary
        counter = {}
        #now we check the character count.
        for char in  range(len(s)):
            counter[s[char]] = counter.get(s[char], 0) + 1
            counter[t[char]] = counter.get(t[char], 0) - 1
        for val in counter.values():
            if val !=0:
                return False
        return True
