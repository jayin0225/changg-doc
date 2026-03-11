import http.server
import socketserver
import os

PORT = 8089

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 处理 404 页面
        if self.path.endswith('.md'):
            # 对于 .md 文件，让 docsify 处理
            pass
        return super().do_GET()

print("Starting server...")
print(f"Working directory: {os.getcwd()}")
try:
    with socketserver.TCPServer(('', PORT), MyHTTPRequestHandler) as httpd:
        print(f'Serving at http://localhost:{PORT}/')
        print('Server started successfully!')
        httpd.serve_forever()
except Exception as e:
    print(f"Error starting server: {e}")
    import traceback
    traceback.print_exc()