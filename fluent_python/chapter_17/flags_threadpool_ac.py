# 把flags_threadpool.py中download_many 函数中的executor.map 方法换成 executor.submit 方法和futures.as_completed 函数

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
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
                # Executor.submit() 方法的参数是一个可调用的对象,调用这个方法后会为传入的可调用对象排期,并返回一个期物。
                future = executor.submit(downlaods_one, cc)
                to_do.append(future)
                msg = 'Scheduled for {}: {}'
                print(msg.format(cc, future))
            
        results = []
        for future in futures.as_completed(to_do):
            # result() 方法。在期物运行结束后调用的:返回可调用对象的结果,或者重新抛出执行可调用的对象时抛出的异常。
            # 此处返回对的是downloads_one的返回值
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

        return len(results)

if __name__ == '__main__':
    main(download_many)