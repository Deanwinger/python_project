"""
    辅助函数， 检测相撞
"""


def aInb(x, x1, x2):
    return (x >= x1) and (x <= x2)

def recIntersects(a, b):
    # if aInb(a.x, b.x, b.x + b.width) or aInb(b.x, a.x, a.width):
    #     print("I ve been here")
    #     if aInb(a.y, b.y, b.y + b.height) or aInb(b.y, a.y, a.y + a.height):
    #         print("why can I")
    #         return True
    # return False
    if a.x > b.x and a.x < b.x + b.width:
        if a.y > b.y and a.y < b.y + b.height:
            return True
    return False 