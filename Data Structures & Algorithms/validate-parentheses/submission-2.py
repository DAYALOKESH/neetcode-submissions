class Solution:
    def isValid(self, s: str) -> bool:
        valid_par = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for char in s:
            if char in valid_par:
                if stack and stack[-1] == valid_par[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
            