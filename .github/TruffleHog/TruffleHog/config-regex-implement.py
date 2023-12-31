# Verification Server Example (Python)

# Unless you run a verification server, secrets found by the custom regex detector will be unverified. 
# Here is an example Python implementation of a verification server for the Regex Detector config-regex-detector.yaml file.


import json
from http.server import BaseHTTPRequestHandler, HTTPServer

AUTH_HEADER = 'super secret authorization header'


class Verifier(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(405)
        self.end_headers()

    def do_POST(self):
        try:
            if self.headers['Authorization'] != AUTH_HEADER:
                self.send_response(401)
                self.end_headers()
                return

            # read the body
            length = int(self.headers['Content-Length'])
            request = json.loads(self.rfile.read(length))
            self.log_message("%s", request)

            # check the match
            if request['hog detector']['adjective'][-1] == 'cool':
                self.send_response(200)
                self.end_headers()
            else:
                # any other response besides 200
                self.send_response(406)
                self.end_headers()
        except Exception:
            self.send_response(400)
            self.end_headers()


with HTTPServer(('', 8000), Verifier) as server:
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
