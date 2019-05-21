 # Leetcode 14. Longest Common Prefix


# 虽然不难, 但这个题目可以多做几次, 有些小细节, 很容易出现错误
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        n = len(strs)
        if not n:
            return ""
        
        if n == 1:
            return strs[0]
        # 此处要找出最短的那个字符串
        pat = strs[0]
        finale = 0
        for i in range(1, n):
            if len(strs[i]) < len(pat):
                pat = strs[i]
                finale = i
        strs.pop(finale)
        pat_n = len(pat)
        print(strs)
        
        s = ""
        for i in range(pat_n):
            pre = pat[:i+1]
            for j in range(n-1):
                if strs[j][:i+1] != pre:
                    return s
            s = pre
        return s
        



if __name__ == "__main__":
    s = ["ca","a"]
    solu = Solution()
    print(solu.longestCommonPrefix(s))