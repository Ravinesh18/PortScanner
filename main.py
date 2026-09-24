import socket

def scan_port(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    results = s.connect_ex((ip, port))
    if results == 0:
        print(f"Port {port} is open on {ip}")   
    s.close()

target_ip = input("Enter the target IP address: ")
for port in range(1, 64000):
    scan_port(target_ip, port)