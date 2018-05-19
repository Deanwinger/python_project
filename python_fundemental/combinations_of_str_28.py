'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
结果请按字母顺序输出。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''

# 题28
# leetcode 类似题46, 47, 60, 567
# 思路: 拿字符串的第一个字符, 然后反复和剩余的换

class Solution(object):
    def str_permutations(self, ss):
        if not ss:
            return []

        if len(ss) == 1:
            return list(ss)
        
        rec = {}
        sslist = list(ss)
        pStr=[]
        for i in range(len(sslist)):
            if sslist[i] in rec.keys():
                continue
            else:
                rec[sslist[i]] = sslist[i]
            temp = self.str_permutations(''.join(sslist[:i]) + ''.join(sslist[i+1:]))
            for j in temp:
                pStr.append(sslist[i]+j)
        print('='*22, 'The length of my_solution is %d ' % len(pStr))
        return pStr


if __name__ == '__main__':
    ss = 'aabd'
    S = Solution()
    print(S.str_permutations(ss))
    # print(S.Permutation(ss))
 