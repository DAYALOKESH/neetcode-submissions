class Solution:
    def isValid(self, s: str) -> bool:
        valid_pair = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        stack = []

        for char in s:
            if char in valid_pair:
                if stack and stack[-1] == valid_pair[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False