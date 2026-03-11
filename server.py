import http.server
import socketserver
import os
import mimetypes
from urllib.parse import unquote

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # URL 解码路径
        decoded_path = unquote(self.path)
        path_without_query = decoded_path.split('?')[0]
        
        # 构建文件系统路径
        if path_without_query.startswith('/'):
            file_path = path_without_query[1:]
        else:
            file_path = path_without_query
            
        if not file_path:
            file_path = 'index.html'
            
        full_path = os.path.join(os.getcwd(), file_path)
        
        # 检查文件是否存在
        if os.path.exists(full_path) and os.path.isfile(full_path):
            # 直接读取并返回文件
            try:
                with open(full_path, 'rb') as f:
                    content = f.read()
                
                # 猜测 MIME 类型
                content_type, _ = mimetypes.guess_type(full_path)
                if not content_type:
                    content_type = 'application/octet-stream'
                
                self.send_response(200)
                self.send_header('Content-Type', content_type)
                self.send_header('Content-Length', len(content))
                self.end_headers()
                self.wfile.write(content)
                return
            except Exception as e:
                self.send_error(500, str(e))
                return
        
        # 文件不存在 - 关键修复
        # 如果是 .md 文件请求，必须返回 404，让 docsify 处理 404 页面
        if file_path.endswith('.md'):
            print(f"[404] Markdown file not found: {file_path}")
            self.send_error(404, 'File not found')
            return
        
        # 其他请求（如页面路由）返回 index.html（SPA 回退）
        index_path = os.path.join(os.getcwd(), 'index.html')
        if os.path.exists(index_path):
            print(f"[SPA Fallback] {self.path} -> index.html")
            try:
                with open(index_path, 'rb') as f:
                    content = f.read()
                
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', len(content))
                self.end_headers()
                self.wfile.write(content)
            except Exception as e:
                self.send_error(500, str(e))
        else:
            self.send_error(404)

print("Starting server...")
os.chdir('docs')
print(f"Working directory: {os.getcwd()}")
try:
    with socketserver.TCPServer(('', 8090), MyHTTPRequestHandler) as httpd:
        print('Serving at http://localhost:8090/')
        print('SPA fallback enabled for history mode')
        print('IMPORTANT: .md 404 errors will trigger docsify notFoundPage')
        print('Server started successfully!')
        httpd.serve_forever()
except Exception as e:
    print(f"Error starting server: {e}")
    import traceback
    traceback.print_exc()
