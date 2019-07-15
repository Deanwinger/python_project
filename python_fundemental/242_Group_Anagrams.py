# leetcode 49. Group Anagrams
# 程序员代码面试指南 P242


class Solution:
    def groupAnagrams(self, strs):
        rec = {}
        for s in strs:
            r = [ord(i) for i in s]
            r.sort()
            r= tuple(r)
            rec.setdefault(r, []).append(s)
            # if rec.get(r) is None:
            #     rec[r] = [s]
            # else:
            #     rec[r].append(s)
            
        res = [r for r in rec.values()]
        return res


if __name__ =='__main__':
    t = ["eat","tea","tan","ate","nat","bat","eat"]
    s = Solution()
    print(s.groupAnagrams(t))