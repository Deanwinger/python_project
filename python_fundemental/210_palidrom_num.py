# leetcode 9



# 很容易, , 关键是s = s*10+l
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x != abs(x):
            return False
            
        n = 0
        s = 0
        original = x
        while True:
            l = x%10
            x = x//10
            s = s*10+l
            if not x:
                break
        return s == original