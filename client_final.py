import socket
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests
import ssl
import os
#res=requests.get('http://192.168.160.187:12345')
#print(res)

class OnMyWatch:
    path = '.'
    def __init__(self):
        self.observer = Observer()
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler,OnMyWatch.path, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
 
        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_closed(Event):
        #f1=open(FileModifiedEvent.src_path,'r')
        filename=Event.src_path.split('/')[-1]
        with open(Event.src_path,'r') as f1:
            filecode=f1.read()
        filename_with_code=filename+'programcontent'+filecode
        start_client(filename_with_code,'192.168.160.219')
        #start_client(filename_with_code,'192.168.177.43')
        #start_client(filename_with_code,'192.168.177.219')
        #with open(r'/home/rohit/sample/'+filename,'w') as f2:
        #    f2.write(a)

def start_client(message,ip):
    #context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    #context.load_verify_locations(os.getcwd()+'/certificate.pem')
    
    #below two codes work
    uclient_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # Create a socket object
    client_socket = ssl.wrap_socket(uclient_socket, cert_reqs=ssl.CERT_REQUIRED, ca_certs=(os.getcwd()+'/certificate.pem'))
    
    #client_socket=context.wrap_socket(uclient_socket, server_hostname=ip)
    # Connect to the server
    host = ip # localhost
    port = 12345
    client_socket.connect((host, port))

    #message = "Hello, server!"          # Send a message to the server
    client_socket.sendall(message.encode())
    

    echoed_message = client_socket.recv(1024)           # Receive and print the echoed message from the server
    print(f"Received from server: {echoed_message.decode()}")

    client_socket.close()               # Close the client socket

if __name__ == "__main__":
    f=OnMyWatch()
    f.run()
