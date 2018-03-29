import sys
import asyncio

from charfinder import UnicodeNameIndex

CRLF = b'\r\n'
PROMPT = b'?> '

index = UnicodeNameIndex()

# 这个协程要传给 asyncio.start_server 函数,接收的两个参数是
# asyncio.StreamReader 对象和 asyncio.StreamWriter 对象
@asyncio.coroutine
def handle_queries(reader, writer):
    while True:
        writer.write(PROMPT)
        yield from  writer.drain()
        data = yield from reader.readline()
        try:
            query = data.decode().strip()
        except UnicodeDecodeError:
            query = '\x00'
        client = writer.get_extra_info('peername')
        print('Received from {}: {!r}'.format(client, query))
        if query:
            if ord(query[:1]) < 32: #如果收到控制字符或者空字符,退出循环。
                break
            lines = list(index.find_description_strs(query))
            if lines:
                writer.writelines(line.encode() + CRLF for line in lines)
            writer.write(index.status(query, len(lines)).encode() + CRLF)

            yield from writer.drain()
            print('Sent {} results'.format(len(lines)))

    print('Close the client socket')
    writer.close()

# def main(address='127.0.0.1', port=2323):
#     port = int(port)
#     loop = asyncio.get_event_loop()
#     server_coro = asyncio.start_server(handle_queries, address,
#                                         port, loop=loop)
#     server = loop.run_until_complete(server_coro)
#     host = server.socket[0].getsockname()
#     print('Serving on {}. Hit CTRL-C to stop.'.format(host))
#     try:
#         loop.run_forever()
#     except KeyboardInterrupt:
#         pass
    
#     print('Server shutting down.')
#     server.close()
#     loop.run_until_complete(server.wait_closed())
#     loop.close()


@asyncio.coroutine
def init(loop, address, port):
    app = web.application(loop=loop)
    app.router.add_route('GET', '/', home)
    handler = app.make_handler()
    server = yield from loop.create_server(handler, address, port)
    return server.sockets[0].getsockname()

def main(address="127.0.0.1", port=8888):
    port = int(port)
    loop = asyncio.get_event_loop()
    host = loop.run_until_complete(init(loop, address, port))
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt: # 按CTRL-C键
        pass
    print('Server shutting down.')
    loop.close()

def home(request):
    query = request.GET.get('query', '').strip()
    print('Query: {!r}'.format(query))
    if query:
        descriptions = list(index.find_descriptions(query))
        res = '\n'.join(ROW_TPL.format(**vars(descr))
                        for descr in descriptions)
        msg = index.status(query, len(descriptions))
    else:
        descriptions = []
        res = ''
        msg = 'Enter words describing characters.'
    html = template.format(query=query, message=msg, result=res)
    print('Sending {} results'.format(len(descriptions))) ➏
    return web.Response(content_type=CONTENT_TYPE, text=html)

if __name__ == '__main__':
    main(*sys.argv[1:])

        

