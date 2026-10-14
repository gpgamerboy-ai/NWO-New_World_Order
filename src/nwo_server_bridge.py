# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class NWOHYBRIDBridgeHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>🛸 NWO CORE PROTOCOL RUNNING CLEANLY</h1></body></html>", "utf-8"))

    def do_POST(self):
        if self.path == "/api/initialize_match":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            json_payload = json.loads(post_data.decode('utf-8'))
            
            response_ack = {
                "server_routing_status": "SUCCESS_ESTABLISHED",
                "allocated_seats": json_payload.get("allocated_seats_count", 7)
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(response_ack), "utf-8"))

def launch_integration_server(port_id=8080):
    server_address = ('', port_id)
    httpd = HTTPServer(server_address, NWOHYBRIDBridgeHandler)
    return httpd

if __name__ == "__main__":
    mock_server = launch_integration_server(port_id=8080)
    print("--- NWO INTEGRATION ROUTER STATUS: ONLINE ---")
