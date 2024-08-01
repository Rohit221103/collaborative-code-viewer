import socket
import os
import ssl
import requests

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
a=s.getsockname()[0] #get ip adress of this machines wlan/eth/ whichever wifi ur connected to
s.close()

def start_server():

           # Create a socket object
    #server_socket = ssl.wrap_socket(server_socket,certfile=(os.getcwd()+'/'+'certificate.pem'), server_side=True, ssl_version=ssl.PROTOCOL_TLS)
    # Bind the socket to a specific address and port
    
    #context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    #context.load_cert_chain((os.getcwd()+'/'+'certificate.pem'),(os.getcwd()+'/'+'key.pem'))
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #server_socket=context.wrap_socket(userver_socket, server_side=True)


    

    host = a  # localhost
    port = 12345
    #res = requests.get('https://'+str(a)+':'+str(port))
    #print(res)
    server_socket.bind((host, port))
    server_socket.listen(5)         # Listen for incoming connections

    print(f"Server listening on {host}:{port}")
    
    while True:
        ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ssl_context.load_cert_chain((os.getcwd()+'/'+'certificate.pem'),(os.getcwd()+'/'+'key.pem'))

        uclient_socket, client_address = server_socket.accept()              # Accept a connection from a client
        print(f"Connection established with {client_address}")

        client_socket = ssl_context.wrap_socket(uclient_socket, server_side=True)
        data = client_socket.recv(1024)         # Receive and echo back data
        if not data:
            break
        #print(f"Received from client: {data.decode()}")
        #print(data.decode(),type(data.decode))

        #filename,filecode
        x=(str(data.decode())).split('programcontent')

        filename,filecode=x[0],x[1]

        #print(filename,filecode)

        with open(os.path.join(os.getcwd(),filename),'w') as f1:
            f1.write(filecode)

        client_socket.sendall("Hello from server".encode())

        client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    start_server()
