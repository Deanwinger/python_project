# leetcode 392. 判断子序列

# 一开始以为是LCS类似的题, 后来转念一想, 其实是个无比简单的题, pass
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        i = 0
        for item in t:
            if s[i] == item:
                i += 1
                
            if i == len(s):
                return True
        return False