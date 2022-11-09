# CS460 Web assignment Part1

This web assignment part1 is making http 1.0 server, which can accept client connections and receive data.

## About me

Hyunsoo Kim
hk486@nau.edu

### What does the code do?

This HTTP/1.1 server is implemented by Python 3.9.13. This server only respond to the GET request.
Except the root request, the server will show the status and message based on [rfc2616](https://www.ietf.org/rfc/rfc2616.html).

### How to compile and run

```shell
1. download the file "http_server.py" and "index.html" in the same directory
2. Turn on the terminal at the root of the http_server.py locaton
3. python3 http_server.py
```
