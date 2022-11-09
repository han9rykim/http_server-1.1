import socket
HOST = '127.0.0.1' # IP address that server is running on 
PORT = 8888 # Port number that the server is listening on​
# Write an http server that prints any data that is sent to 

# handelRequest fucntion that handles the data server received
# and return the response
def handleRequest(received_data):
  # general_header in the request
  general_header = ["Cache-Control", "Connection", "Date", "Pragma",
  "Trailer", "Transfer-Encoding", "Upgrade", "Via", "Warning"]

  # request_header in the request
  request_header = ["Accept", "Accept-Charset", "Accept-Encoding",
  "Accept-Language", "Authorization", "Expect", "From", "Host", "If-Match",
  "If-Modified-Since", "If-None-Match", "If-Range", "If-Unmodified-Since",
  "Max-Forwards", "Proxy-Authorization", "Range", "Referer", "TE", "User-Agent"]

  # entity_header in the request
  entity_header = ["Allow", "Content-Encoding", "Content-Language",
  "Content-Length", "Content-Location", "Content-MD5", "Content-Range",
  "Content-Type", "Expires", "Last-Modified"]

  # headers list is the list of all the headers 
  # from general header, request header and entity header
  headers = general_header + request_header + entity_header

  # method list is the possible methods that can be used in the request
  method = ["OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT"]

  # request_data is the list that is used to store the data from the request
  request_data = received_data.decode("utf-8").split("\r\n")

  # checking if the header in the request_data is valid
  # doesn't check the extension header so checked as commented
  
  header_valid_flag = True
  # for header in request_data[1:-1]:
  #   if request_data.index(header) == -2 and header == "":
  #     continue
  #   header_name = header.split(":")
  #   if header_name[0] not in headers:
  #     header_valid_flag = False
  #     print(header_name[0])
  #     break

  # print the request_data
  print(request_data)

  # request_line is the request_data[0] 
  # which is the first line of the request
  request_line = request_data[0].split(" ")
  
  # check if the method is valid
  method_flag = False
  # check if the method is GET
  is_method_get = False
  # check if the request_uri starts with "/"
  request_uri_flag = False
  # check if the request_uri is just "/"
  is_uri_valid = False
  # check if the http_version is valid
  http_version_flag = False
  # if the length of request_line is less than 3
  if len(request_line) < 3:
    # return the response with 400 Bad Request
    status_line = "HTTP/1.1 400 Bad Request\r\n"
    message_body = "<html><body><h1>HTTP/1.1 400 Bad Request</h1></body></html>"
    response = status_line + message_body
    # return the response
    return response
  # check the method
  if request_line[0] in method:
    # set the method_flag to True
    method_flag = True
    # if the method is GET
    if request_line[0] == "GET":
      # set the is_method_get to True
      is_method_get = True
    # if the method is not GET
    else:
      # set the is_method_get to False
      is_method_get = False
  # if the method is not valid
  else:
    # set the method_flag to False
    method_flag = False
  
  # check if the Request-URI is valid
  # check if the Request-URI starts with /
  if len(request_line[1]) > 0 and request_line[1][0] == "/":
    # set the request_uri_flag to True
    request_uri_flag = True
    # if the Request-URI is just /
    if len(request_line[1]) == 1:
      # set the is_uri_valid to True
      is_uri_valid = True
    else:
      is_uri_valid = False

  # check if the HTTP-Version is valid
  if request_line[2] != "HTTP/1.1":
    # if the HTTP-Version is not valid
    # set the http_version_flag to False
    http_version_flag = False
  # if the HTTP-Version is valid
  else:
    # set the http_version_flag to True
    http_version_flag = True

  # if the request is valid
  if method_flag and request_uri_flag and http_version_flag and header_valid_flag:
    # if the request is GET
    if is_method_get:
      # if the request_uri is just /
      if is_uri_valid:
        # return the response with 200 OK
        status_line = "HTTP/1.1 200 OK\r\n"
        message_body = ""
        # read index.html file and store the data in message_body
        with open("index.html") as f:
          content_list = f.readlines()
        for content in content_list:
          message_body += content
      
      else:
        # return the response with 404 Not Found
        # because the file is doesn't exist
        status_line = "HTTP/1.1 404 Not Found\r\n"
        message_body = "<html><body><h1>HTTP/1.1 404 Not Found</h1></body></html>"
    # if the request is not GET
    else:
      # as the methods except the GET are not implemented
      # return the response with 501 Not Implemented
      status_line = "HTTP/1.1 501 Not Implemented\r\n"
      message_body = "<html><body><h1>HTTP/1.1 501 Not Implemented</h1></body></html>"
  # if the request is not valid
  else:
    # if the method is not valid
    if not method_flag:
      # return the status 405 Method Not Allowed
      status_line = "HTTP/1.1 405 Method Not Allowed\r\n"
      message_body = "<html><body><h1>HTTP/1.1 405 Method Not Allowed</h1></body></html>"
    
    # if the request_uri is not valid
    elif not request_uri_flag:
      # return the status 400 Bad Request
      status_line = "HTTP/1.1 400 Bad Request\r\n"
      message_body = "<html><body><h1>HTTP/1.1 400 Bad Request</h1></body></html>"
    # if the http_version is not valid
    elif not http_version_flag:
      status_line = "HTTP/1.1 505 HTTP Version Not Supported\r\n"
      message_body = "<html><body><h1>HTTP/1.1 505 HTTP Version Not Supported</h1></body></html>"
    # if the header is not valid
    elif not header_valid_flag:
      status_line = "HTTP/1.1 400 Bad Request\r\n"
      message_body = "<html><body><h1>HTTP/1.1 400 Bad Request</h1></body></html>"
  # before the message_body crlf is added
  message_body = "\r\n"+message_body
  # response is the status_line + message_body
  response = status_line + message_body
  # return response
  return response


# Step 1.  Create a server socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  # Step 2.  Bind the server socket to the port and IP address
  s.bind((HOST,PORT))

  # Step 3.  Listen for incoming client connections
  s.listen()
  # Step 4.  Accept client connection
  while True:
    conn, addr = s.accept()
    # Step4b. Receive data and use handleRequest function to handle the data
    data = conn.recv(1024)
    
    if not data:
      print(data)
      conn.sendall(data)
      break
    
    # Step 4c. Make the response using handleRequest function
    response = handleRequest(data)
    # Step 4d. Send the response to the client
    conn.send(response.encode())
    # Step 5.  Close the connection
    conn.close()
  # Step 6.  Close the server socket
  s.close()
