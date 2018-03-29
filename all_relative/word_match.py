import re


def check_user_input(string):
    """检查用户输入"""
    string = string.strip()
    if re.match(r"^[a-zA-Z\u4e00-\u9fa5]{2,15}$", string):
        return True
    else:
        raise Exception(400, "参数不合法")





if __name__ == "__main__":
    string = "大中华区"
    print(check_user_input(string))