# leetcode 20 Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stack = []
        n = len(s)
        i = 1
        stack.append(s[0])
        while i < n:
            if stack and self.is_pair(stack[-1], s[i]):
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
            
        if len(stack) == 0:
            return True
        else:
            return False
        
    def is_pair(self, left, right):
        return (left=='(' and right ==')') or (left=='[' and right ==']') or (left=='{' and right =='}')