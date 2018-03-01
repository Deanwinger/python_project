from concurrent import futures

from flags import save_flags, get_flag, show, main

MAX_WORKERS = 20

def downlaods_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flags(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        #map 方法返回一个生成器,因此可以迭代,获取各个函数返回的值。
        res = executor.map(downlaods_one, sorted(cc_list)) 
    return len(list(res))

if __name__ == '__main__':
    main(download_many)