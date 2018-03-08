#测试要点, 1: 基本的get请求, 2, 下订单, 购买, 连续动作的模拟
# 代码要点 a.测试时需要记录的信息, b.exception
# 测试版本 多线程版, concurrent.futures 版

#多线程版
import requests
from concurrent import futures
from random import randint

from user_info import users_info, uid_list


#start from 100
MAX_WORKER = 100

#测试的主要接口
base_url = "https://api-t.lansheng8.com/"
urls = [
    'article?notice_type=4&page=1&limit=8',
    'order_fund?action=user_fund&user_uid=265&valid=1&page=1&limit=10',
    'user/265',
    'fund',
    'farlinks',
    'fund/586',
    'order_fund?action=duration&duration=1&page=1&limit=13',
    'fund_dividend?action=duration&duration=1&page=1&limit=13',
    'standard_agreement?action=all&page=1&limit=13',
    'redpacket?action=all',
    'cash_flow?page=1&limit=10',
]

def req_source(url):
    user_uid, accesse_token = get_user(users_info, uid_list)
    headers = {'UserID': user_uid, 
               'AccessToken': accesse_token}
    res = requests.get(url, headers=headers)
    return res.status_code

def main():
    url_list = get_url_list(urls)
    with futures.ThreadPoolExecutor(MAX_WORKER) as executor:
        res = executor.map(req_source, url_list)
        print()
    return 
    
    
def get_user(users_info, uid_list):
    length = len(users_info)
    index = randint(0, length)
    user_uid = uid_list[index]
    user_token = users_info[user_uid]
    return user_uid, user_token


def get_url_list(urls):
    n = 1000
    url_list = []
    while n > 0:
        index = randint(0, 11)
        url_list.append(urls[index])
    return url_list        

    # for url in urls:
    #     try:
    #         url = base_url + url
    #         res = req_source(url)  
    #     except requests.exceptions.HTTPError as exc:
    #         error_msg = 'HTTP error {res.status_code} - {res.resson}'
    #         error_msg = error_msg.format(res=exc.response)
    #     except requests.exceptions.ConnectionError as exc:
    #         error_msg = 'Connection error'
    #     else:
    #         print(res.json())
    #         print(res.status_code)


#另一种实现, 请求前确认,user和url, 待实现
if __name__ == '__main__':
    main()




