import socket
#client setup
HOST = "127.0.0.1"   #server address
PORT = 5000    #Server port

#create socket (IPv4 + TCP)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
#CONNECT TO SERVER

#SEND REQUEST
message = "hey server"
client_socket.sendall(message.encode())
#receive response
response = client_socket.recv(1024).decode()
print(f"Server Response: {response}")

#close connection
client_socket.close()