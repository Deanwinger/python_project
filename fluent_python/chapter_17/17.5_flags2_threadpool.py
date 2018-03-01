import collections
from concurrent import futures

import requests
import tqdm

# 从flags2_common 模块中导入一个函数和一个 Enum
from flags2_common import main, HTTPStatus
# from flags2_sequential import download_one

Result = namedtuple('Result', ['status', 'cc'])


def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = requests.get(url)
    if resp.status_code != 200:
        resp.raise_for_status()
    return resp.content

def download_one(cc, base_url, verbose=False):
    try:
        image = get_flag(base_url, cc)
    except requests.exceptions.HTTPError as exc:
        res = exc.response
        if res.status_code == 404:
            status = HTTPStatus.not_found
            msg = 'not found'
        else:
            raise
    else:
        save_flags(image, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'OK'
    
    if verbose:
        print(cc, msg)
    
    return Result(status, cc)