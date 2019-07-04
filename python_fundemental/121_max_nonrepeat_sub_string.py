# leetcode 3. 无重复字符的最长子串

'''
题目解析
方法一:
建立一个 HashMap ，建立每个字符和其最后出现位置之间的映射，然后再定义两个变量 
res 和 left ，其中 res 用来记录最长无重复子串的长度，left 指向该无重复子串左边
的起始位置的前一个，一开始由于是前一个，所以在初始化时就是 -1。

接下来遍历整个字符串，对于每一个遍历到的字符，如果该字符已经在 HashMap 中存在了，
并且如果其映射值大于 left 的话，那么更新 left 为当前映射值，然后映射值更新为
当前坐标i，这样保证了left始终为当前边界的前一个位置，然后计算窗口长度的时候，
直接用 i-left 即可，用来更新结果 res 。

方法二:
建立一个256位大小的整型数组 freg ，用来建立字符和其出现位置之间的映射。

维护一个滑动窗口，窗口内的都是没有重复的字符，去尽可能的扩大窗口的大小，窗口不停的向右滑动。

（1）如果当前遍历到的字符从未出现过，那么直接扩大右边界；
（2）如果当前遍历到的字符出现过，则缩小窗口（左边索引向右移动），然后继续观察当前遍历到的字符；
（3）重复（1）（2），直到左边索引无法再移动；
（4）维护一个结果res，每次用出现过的窗口大小来更新结果 res，最后返回 res 获取结果。
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n = len(s)
        
        # if n <= 1:
        #     return n
        
        # i = 0
        # j = 1
        # cmax = cur = 1
        # while j<n:
        #     print(cur)
        #     if s[j] == s[i]:
        #         i += 1
        #     else:
        #         cur += 1
        #     j += 1
        #     if cmax < cur:
        #         cmax = cur
        # return cmax


if __name__=='__main__':
    s = "tmmzuxt"
    solu = Solution()
    print(solu.lengthOfLongestSubstring(s))