# 程序员代码面试指南 P13
# 一个栈实现另一个栈的排序, 栈顶到底, 从大到小排序



def sortStack(stack):
    if not stack:
        return 
    aux = []
    while stack:
        e = stack.pop()
        if not aux:
            aux.append(e)
        else:
            while aux and aux[-1] < e:
                stack.append(aux.pop())
            aux.append(e)
    while aux:
        stack.append(aux.pop())
    return 


if __name__=="__main__":
    from random import randint
    n = 20
    while n:
        stack = []
        for _ in range(50):
            stack.append(randint(0, 1000))
            ts = list(stack)
        # print(stack)
        # stack = [3,1, 4, 2, 5]
        sortStack(stack)
        res = sorted(ts)
        # print(stack)
        assert res == stack
        print(res == stack) 
        n -= 1