# leetcode 131. 分割回文串

'''
class Solution {
    List<List<String>> res = new ArrayList<>();

    public List<List<String>> partition(String s) {
        if(s==null||s.length()==0)
            return res;
        dfs(s,new ArrayList<String>(),0);
        return res;
    }

    public void dfs(String s,List<String> remain,int left){
        if(left==s.length()){  //判断终止条件
            res.add(new ArrayList<String>(remain));  //添加到结果中
            return;
        }
        for(int right=left;right<s.length();right++){  //从left开始，依次判断left->right是不是回文串
            if(isPalindroom(s,left,right)){  //判断是否是回文串
                remain.add(s.substring(left,right+1));   //添加到当前回文串到list中
                dfs(s,remain,right+1);  //从right+1开始继续递归，寻找回文串
                remain.remove(remain.size()-1);  //回溯，从而寻找更长的回文串
            }
        }
    }
    /**
    * 判断是否是回文串
    */
    public boolean isPalindroom(String s,int left,int right){
        while(left<right&&s.charAt(left)==s.charAt(right)){
            left++;
            right--;
        }
        return left>=right;
    }
}
'''

# 2019-5-6, 非常典型的回溯法, 好好体会
class Solution:
    def partition(self, s: str):
        if not s:
            return [[]]
        
        rec = []
        g = []
        self.get_strlist(s, rec, g)
        return g
        
        
    def get_strlist(self, s, rec=[], g=[]):
        if not s:
            g.append(list(rec))
            return
        
        n = len(s)
        for i in range(n):
            if self.is_palindrome(s[:i+1]):
                rec.append(s[:i+1])
                self.get_strlist(s[i+1:],rec, g)
                rec.pop()
        return
    
    def is_palindrome(self, s):
        return s == s[::-1]



if __name__=='__main__':
    s = Solution()
    strings = "aab"
    print(s.partition(strings))