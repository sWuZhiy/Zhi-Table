from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MockHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode('utf-8') if length > 0 else ''
        try:
            data = json.loads(body) if body else {}
        except Exception:
            data = {"raw": body}

        # 构造一个示例 plans 返回
        plans = [
            {
                "id": "mock1",
                "title": "模拟·背词",
                "dayOfWeek": 2,
                "startTime": "14:00",
                "endTime": "16:00",
                "color": "#f59e0b",
                "location": "",
                "isAiGenerated": True
            }
        ]

        resp = {
            "plans": plans,
            "reasoning": "本地 mock：已为您生成示例 plans"
        }

        self._set_headers()
        self.wfile.write(json.dumps(resp, ensure_ascii=False).encode('utf-8'))

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MockHandler)
    print('Mock server running on http://localhost:8000')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Mock server stopped')
