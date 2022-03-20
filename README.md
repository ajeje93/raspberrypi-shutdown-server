# Raspberry Shutdown Server

Just a simple HTTP server to shutdown/reboot your Raspberry PI.

Start with command:

```bash
SHUTDOWN_SERVER_PORT="<port>" SHUTDOWN_SERVER_API_KEY="<your api key>" python server.py
```

The server will be running on port specified by env `SHUTDOWN_SERVER_PORT`.

Make an HTTP GET with header `x-api-key` set to `SHUTDOWN_SERVER_API_KEY` value on path:

* `/shutdown` to shutdown
* `/reboot` to reboot
