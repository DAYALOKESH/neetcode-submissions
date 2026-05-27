class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = ""
        for char in s:
            if char.isalnum():
                palin= palin + char.lower()

        left = 0
        right = len(palin)-1

        while right >= left:
            if palin[right]!=palin[left]:
                return False
            left += 1
            right -=1
        
        return True