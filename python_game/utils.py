"""
    辅助函数， 检测相撞
"""


def recIntersects(a, b):
    if a.x > b.x and a.x < b.x + b.width:
        if a.y > b.y and a.y < b.y + b.height:
            return True
    return False 