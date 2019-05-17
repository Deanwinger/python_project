# leetcode 455


# 极其简单, pass
class Solution:
    def findContentChildren(self, s, g) -> int:
        s = sorted(s)
        g = sorted(g)
        counter = 0
        i = j = 0
        print(s)
        print(g)
        while i< len(s) and j < len(g):
            if g[j] >= s[i]:
                counter += 1
                i += 1                
            j += 1
                
        return counter

if __name__=='__main__':
    g = [10,9,8,7]
    s = [5,6,7,8]
    solu = Solution()
    print(solu.findContentChildren(g, s))

