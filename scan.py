#! /usr/bin/python3
import sys
import socket


MULTIPLE=1
SINGLE=0

def scan(sock, ip, port):
    if sock.connect_ex((ip, port)) == 0:
        sock.close()
        return [port]
    else:
        return None


def scan_range(ip, port_alpha, port_omega):
    buffer = list()
    for port in range(port_alpha, port_omega):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if sock.connect_ex((ip, port)) == 0:
            buffer.append(port)
            sock.close()

    if(len(buffer)!=0):
        return buffer
    else:
        return None


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sys.argv[1] == "-m" or sys.argv[1] == "--multiple":
        flag = MULTIPLE
        IP = sys.argv[2]
        PORT_RANGE = sys.argv[3]
        alpha = PORT_RANGE.split('-')[0]
        omega = PORT_RANGE.split('-')[1]
        res = scan_range(IP, int(alpha), int(omega))

    else:
        flag = SINGLE
        IP = sys.argv[1]
        PORT = sys.argv[2]
        res = scan(sock, IP, int(PORT))

    if res!=None:
        for port in res:
            print(f'[+] Port {port}[open]')
    
    else:
        if flag == MULTIPLE:
            print("[*] No ports are opened in the specified range!")
        elif flag == SINGLE:
            print(f"[*] Port {sys.argv[2]} is closed!")

        

    



        
    
