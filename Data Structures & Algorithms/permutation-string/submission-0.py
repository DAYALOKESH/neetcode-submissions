class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        l = 0
        for i in range(len(s2)-len(s1)+1):
            substr = s2[i:i+len(s1)]
            substr = sorted(substr)

            if s1 == substr:
                return True
        return False