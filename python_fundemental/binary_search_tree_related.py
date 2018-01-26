'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点
'''

#题24
#LeetCode 类似题98， 145

class Solution(object):
    def VerifySquenceOfBST(self, array):
        #这个终止判断条件有点奇怪
        if not array or len(array)==1:
            return True

        root = array[-1]
        end = len(array)-1 #root 节点index
        i = 0
        while i < end:
            if array[i] > root:
                break
            i += 1
        j = i
        while j < end:
            if array[j] < root:
                return False
            j += 1
        left = self.VerifySquenceOfBST(array[:i])
        right = self.VerifySquenceOfBST(array[i:end-1])
        return left & right

if __name__=='__main__':
    # array = [5, 7, 6, 9, 11, 10, 8]
    # array = [7, 4, 6, 5]
    array = [4, 6, 7, 5]
    # array3 = [1, 2, 3, 4, 5]
    S = Solution()
    print(S.VerifySquenceOfBST(array))
        
