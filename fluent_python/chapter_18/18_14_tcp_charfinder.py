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


        

