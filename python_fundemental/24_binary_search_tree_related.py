'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点
'''

#题24
#LeetCode 类似题98， 145

class Solution(object):
    # 解法1
    def VerifySquenceOfBST(self, array):
        """此方法是通过每次得到一颗子树， 遍历slice（子树），比较与root的大小"""
        #   这个终止判断条件有点奇怪
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

# 8.20重写， by self, 此才是合格的版本
class Solution:
    def VerifySquenceOfBST(self, array):
        # write code here
        if not array:
            return False
        return self.is_valid(array)
    
    def is_valid(self, array):
        if not array:
            return True
        
        root_index = len(array)-1
        root = array[-1]
        
        i = 0
        while array[i] < root:
            i += 1
        
        j = i
        while j < root_index:
            if array[j] < root:
                return False
            j += 1
            
        left = self.is_valid(array[:j])
        right = self.is_valid(array[j:root_index])
        return left and right


if __name__=='__main__':
    array1 = [5, 7, 6, 9, 11, 10, 8]
    array2 = [7, 4, 6, 5]
    array3 = [4, 6, 7, 5]
    array4 = [1, 2, 3, 4, 5]
    array5 = [4,6,12,8,16,14,10]
    S = Solution()
    print(S.VerifySquenceOfBST(array5))
    print(S.is_bstree(array5))
    print("="*30)

    # print(S.VerifySquenceOfBST(array2))
    # print(S.is_bstree(array2))
    # print("="*30)

    # print(S.VerifySquenceOfBST(array3))
    # print(S.is_bstree(array3))
    # print("="*30)

    # print(S.VerifySquenceOfBST(array4))
    # print(S.is_bstree(array4))
        
