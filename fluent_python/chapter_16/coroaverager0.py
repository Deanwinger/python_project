from functools import wraps

def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def averager():
    average = None
    count = 0
    total = 0.0
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count  





if __name__ == '__main__':
    averager()