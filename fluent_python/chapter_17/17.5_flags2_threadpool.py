import collections
from concurrent import futures

import requests
import tqdm

# 从flags2_common 模块中导入一个函数和一个 Enum
from flags2_common import main, HTTPStatus

Result = namedtuple('Result', ['status', 'cc'])

DEFAULT_CONCUR_REQ = 30
MAX_CONCUR_REQ = 1000

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


def download_many(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    with futures.ThreadPoolExecutor(max_workers=concur_req) as executor:
        to_do_map = {}
        for cc in sorted(cc_list):
            future = executor.submit(download_one, 
                                    cc, base_url, verbose)
            to_do_map[future] == cc
        done_iter = futures.as_completed(to_do_map)
        if not verbose:
            done_iter = tqdm.tqdm(done_iter, total=len(cc_list))
        for future in done_iter:
            try:
                res = future.result()
            except requests.exceptions.HTTPError as exc:
                error_msg = 'HTTP {res.status_code} - {res.reason}'
                error_msg = error_msg.format(res=exc.response)
            except requests.exceptions.ConnectionError as exc:
                error_msg = 'Connection error'
            else:
                error_msg = ''
                status = res.status
            
            counter[status] += 1
            if verbose and error_msg:
                cc = to_do_map[future]
                print('*** Error for {}: {}'.format(cc, error_msg))
    return counter