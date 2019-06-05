# 程序员代码面试指南 P8 好好体会递归
# 逆序一个栈

def get_last_element(stack):
    res = stack.pop()
    if not stack:
        return res
    else:
        last = get_last_element(stack)
        stack.append(res)
        return last

def reverse(stack):
    if not stack:
        return

    i = get_last_element(stack)
    print(i)
    reverse(stack)
    stack.append(i)
    return


if __name__=="__main__":
    stack = [1,2,3,4,5]
    reverse(stack)
    print(stack)