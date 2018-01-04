'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

class Solution(object):
    #内置replace函数
    def blank_replace(self, s):
        if type(s) != str:
            return
        r = s.replace(' ', '%20')
        return r

    #书中的思路
    def replace_blank(self, s):
        if not isinstance(s,str) or len(s) <= 0 or s == None:
            return ""

        length = len(s)
        numspace = 0
        for i in s:
            if i == ' ':
                numspace += 1
        new_length = length + numspace*2
        new_s = new_length * [None]
        ptr1 = length - 1
        ptr2 = new_length - 1
        for i in range(ptr1, -1, -1):
            if s[i] == ' ':
                new_s[ptr2] = '0'
                new_s[ptr2-1] = '2'
                new_s[ptr2-2] = '%'
                ptr2 -= 3
            else:
                new_s[ptr2] = s[i]
                ptr2 -= 1
        return new_s
                
                



if __name__ == '__main__':
    s1 = 'We Are Happy'
    s2 = ' We Are Happy'
    s3 = ''
    s4 = 'We Are Happy '
    s5 = '  '
    repl = Solution()
    # print(repl.blank_replace(s))
    print(repl.replace_blank(s1))
    print(repl.replace_blank(s2))
    print(repl.replace_blank(s3))
    print(repl.replace_blank(s4))
    print(repl.replace_blank(s5))