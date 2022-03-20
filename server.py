#!/usr/bin/python3

import BaseHTTPServer
import os

class HttpHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(self):
    if self.headers.get('x-api-key') != os.environ['SHUTDOWN_SERVER_API_KEY']:
      self.send_response(401)
      self.send_header("Content-type", "application/json")
      self.end_headers()
      self.wfile.write("{\"message\": \"Unauthorized\"}")
    else:
      self.send_response(200)
      self.send_header("Content-type", "application/json")
      self.end_headers()
      if self.path == "/shutdown":
        self.wfile.write("{\"status\": \"SHUTTING_DOWN\"}")
        os.popen("sudo shutdown -h now")
      elif self.path == "/reboot":
        self.wfile.write("{\"status\": \"REBOOTING\"}")
        os.popen("sudo reboot")
      else:
        self.wfile.write("{\"status\": \"IGNORED\"}")

BaseHTTPServer.HTTPServer(("", int(os.environ['SHUTDOWN_SERVER_PORT'], 10)), HttpHandler).serve_forever()
