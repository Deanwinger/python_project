import re
from pprint import pprint


# 删除字符串中不需要的字符
# strip() 方法能用于删除开始或结尾的字符。 
# lstrip() 和 rstrip() 分别从左和从右执行删除操作。 这些方法默认会去除空白字符
def update_profile_1():
    banks_list = {}
    banks_li = []
    with open("/home/ubuntu/alan/banks.txt", 'r') as fp:
        banks = fp.readlines()
        # print(banks)
        for b in banks:
            c = b.strip()
            banks_li.append(c)
        # print(banks_li)

def update_profile_2():
    banks_li = []
    banks_bk = []
    banks_bs = []
    with open("/home/ubuntu/alan/banks.txt", 'r') as fp:
        # generator
        lines = (line.strip() for line in fp)
        for line in lines:
            banks_li.append(line)
        #处理中间的空格，使用 replace() 方法
        for s in banks_li:
            a = s.replace(' ', '')
            banks_bk.append(a)
        # 用正则表达式替换引号\"
        for b in banks_bk:
            d = re.sub('\"', '', b)
            banks_bs.append(d)
        print(banks_bs)


# 直接正则匹配
def update_profile_3():
    banks = {}
    with open("/home/ubuntu/alan/banks.txt", 'r') as fp:
        # generator
        lines = (line.strip() for line in fp)
        for line in lines:
            try:
                line = line.replace(' ', '')
                print(line)
                re_bank = re.compile(r'^\"(\d{4})\"\"(\w+)\"$')
                s_bank = re_bank.match(line).groups()
                banks[s_bank[1]] = s_bank[0]
            except AttributeError:
                pass
        print(banks)

#处理, 生成returned dict
def gene_pre(path):
    res = []
    dis = []
    with open(path, encoding='utf-8') as fp:
        rec = fp.readlines()
        for i in rec:
            if i == '\n':
                continue
            s = i.strip().split("=")
            if s[0].startswith("#"):
                continue
            res.append(s[0].strip())
        # print(res)    

        for r in res:
            print(r+',')

        # for r in res:
        #     print('self.'+ r + " = " + r )      
    return res

def gene_dict(path):
    res = gene_pre(path)
    
    for r in res:  
        key = '"' + r + '"'          
        value = 'self.' + r
        item =  key + ': ' + value + ','
        print(item)

def gene_g_params(path):
    
    res = gene_pre(path)
    rec = []
    for r in res:
        strs = r+ ' = g.params[' +"'"+ '%s' % r + "'" + ']'
        rec.append(strs)
    for i in rec:
        print(i)





if __name__ == "__main__":
    # update_profile_1()
    # update_profile_2()
    # update_profile_3()
    # path = 'D:\python-related\python_fundemental\\test.txt'
    path = '/home/ubuntu/alan/python_related/python_fundemental/test.txt'
    # gene_pre(path)        # 1---字符串  2---构造self.uid = uid  3---list
    gene_dict(path)         #构造出如'"uid": self.uid,'
    # gene_g_params(path)     #构造key = g.params["key"]
