import http.server
import socketserver
import os

PORT = 8089

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 处理 404 页面 - 支持 HTML5 History 模式
        if not self.path.endswith(('.html', '.js', '.css', '.png', '.jpg', '.jpeg', '.gif', '.ico', '.md')):
            # 对于非静态文件请求，返回 index.html
            self.path = '/index.html'
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