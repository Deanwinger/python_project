import json
import requests

headers = {
    "X-LC-Id": '4cROByWxr8AfwE8KXoHlCnI6-gzGzoHsz',
    "X-LC-Key": 'q3LYtpmW69TNLIM0qkO2mFMD',
    "Content-Type": "application/json",
}

# 请求发送验证码 API
REQUEST_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/requestSmsCode'

# 请求校验验证码 API
VERIFY_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/verifySmsCode/'

def send_message(phone):
    """
    通过 POST 请求 requestSmsCode API 发送验证码到指定手机
    :param phone: 通过网页表单获取的电话号
    :return:
    """
    data = {
        "mobilePhoneNumber": phone,
    }
    r = requests.post(REQUEST_SMS_CODE_URL, data=json.dumps(data), headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False


def verify(phone, code):
    target_url = VERIFY_SMS_CODE_URL + "%s?mobilePhoneNumber=%s" % (code, phone)
    r = requests.post(target_url, headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False
