import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET=IP adress #SOCK_STREAM=TCP
server.bind(('localhost' , 1002))  #127.0.0.1
server.listen()

client_socket,client_address=server.accept()


file=open("server_image.png","wb")
image_chunk=client_socket.rev(2048)

while image_chunk:
    file.write(image_chunk)
    image_chunk=client_socket.recv(2048)


file.close()
client_socket.close()
