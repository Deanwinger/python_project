from http.server import HTTPServer, BaseHTTPRequestHandler
import os, sys

class RequestHandler(BaseHTTPRequestHandler):
    Error_Page = """\
    <html>
    <body>
    <h1>Error accessing {path}</h1>
    <p>{msg}</p>
    </body>
    </html>
    """

    def do_GET(self):
        try:
            # 请求的相对路径保存在self.path
            if self.path == '/' or '/index.html':
                full_path = os.getcwd() + '\index.html'
                print(full_path)

            if not os.path.exists(full_path):
                raise ServerException("'{0}' not found".format(self.path))
            elif os.path.isfile(full_path):
                self.handle_file(full_path)
            else:
                raise ServerException("Unknown object '{0}'".format(self.path))
        except Exception as e:
            self.handle_error(e)

    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)
    
    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content)

    def send_content(self, content):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

class ServerException(Exception):
    '''服务器内部错误'''
    pass














if __name__ == '__main__':
    serverAddress = ('', 8853)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()