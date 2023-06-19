# Reverse Proxy Server

This is a simple reverse proxy server implemented in Python. It acts as an intermediary between clients and a target server, forwarding client requests to the target server and returning the server's response to the clients.

## Features

- Handles HTTP GET and POST requests.
- Supports forwarding requests to a specified hostname.
- Performs header manipulation, allowing modification or filtering of request and response headers.
- Implements multi-threading for concurrent request handling.
- Provides error handling for request failures.

## Warning

This reverse proxy server is intended for educational and development purposes. It is not recommended for production environments or handling sensitive data. Use it at your own risk.

## Requirements

- Python 3.x
- Requests library (`pip install requests`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/gkhantyln/ReverseProxyServer.git
   cd ReverseProxyServer

2. Modify the `hostname` variable in the `proxy_reverse.py` file to specify the target server's hostname.
3. Run the server:

   ```bash
   python3 ReverseProxyServer.py --port 9999
  
You can optionally specify the port number using the `--port` flag. The `default` port is `9999`.

4. Access the reverse proxy server by sending HTTP requests to `http://localhost:9999`.

## Configuration
You can customize the behavior of the reverse proxy server by modifying the following variables in the proxy_reverse.py file:

`hostname`: Specifies the target server's hostname.
`port`: Specifies the port number for the reverse proxy server to listen on.

## Limitations
This reverse proxy server only supports basic HTTP GET and POST requests.
It may not handle all types of HTTP headers and request methods.
SSL/TLS encryption is not implemented in this server.
License
This project is licensed under the MIT License.

Feel free to fork, modify, and distribute the code according to the terms of the license.

## Disclaimer
This reverse proxy server comes with no guarantees or warranties. Use it at your own risk. The authors are not liable for any damages or losses arising from its use.

