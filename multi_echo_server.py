import socket
import time 
from multiprocessing import Process 

HOST=""
PORT=8001
BUFFER_SIUZE=1024

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as S:
        s.setsopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.listen(2)
        while TRUE:
            conn,addr=s.accept()
            p=Process(target=handle_echo,args=(addr,conn))
            p.daemon=Ture
            p.start()
            print("Started process",p)
            
def handle_echo(addr,conn):
    print("Connected by",addr)
    full_data+conn.recv(BUFFER_SIZE)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUTRDWR)
    conn.close()
if __name__ == "__main__":
    main()