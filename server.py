import socket
#server setup
HOST = "127.0.0.1"  #localhost
PORT = 5000    #port to listen on

#create socket (IPv4 + TCP)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))   #Bind to address
server_socket.listen()   #start listening
print(f"Server listening on {HOST}: {PORT}")

while True:
  conn,addr = server_socket .accept()
  #Accept connection
  print(f"connected by (addr)")
  #receive message from client
  data = conn.recv(1024).decode()
  print(f"Receive: (data)")
  #send response
response = "Hello from server!"
conn.sendall(response.encode())
#close connection
conn.close()
