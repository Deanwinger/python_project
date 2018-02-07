#思路 ： 将输入的数字作为字符串 进行四位四位的输出 ，使用函数 方便再次调用
#输出后，统一对结果进行去 零 优化，分别列出输出的各种情况 一个零 两个零  三个零

dict1={"0":"零","1":"壹","2":"贰","3":"叁","4":"肆","5":"伍","6":"陆","7":"柒","8":"捌","9":"玖"}
dict2={"0":"","1":"拾", "2":"佰",  "3":"仟" }

def fourchar(s):
    res=''
    for i in range(0,len(s)):
        res=res+dict1[s[i]]+dict2[str(len(s)-i-1)]
    return res
#四个字符一次输出

def func(result):
    s1= result.replace("零仟零佰零拾零","").replace("零佰零拾零","").replace("零拾零","")  
    s2= s1.replace("零仟零佰零拾","零").replace("零仟零佰","零").replace("零佰零拾","零")
    s3= s2.replace("零仟","零").replace("零佰","零").replace("零拾","零").replace("零万","万").replace("拾零","拾")
    return s3
#格式化字符串 

def res(a):
    if (len(a)/4.0 >1):
        s=''
        t=''
        result=''
        s= a[:-4]
        t= a[-4:]
        result= fourchar(s)+"万"+fourchar(t)
    else:
        result= fourchar(a)
    return result
#分片输出

if __name__=='__main__':
    a='999999990'

    if len(a) >= 9:
        print("超过最大限额")
    if (int(a) >0):
        print(func(res(a))+"圆")
    else:
        b=str(int(a)*(-1))
        print("负"+func(res(b))+"圆")