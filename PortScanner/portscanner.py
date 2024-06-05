import socket
import termcolor


def scan(target,ports):
    print("\n" + ' Starting Scan For ' + str(target))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened "+ str(port))
        sock.close()
    except:
        pass

targets = input("[*] Enter Targets to Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want to Scan: "))
if ',' in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(" "), ports)
else:
    scan(targets, ports)

# import socket
# import termcolor
# import nmap

# def scan(target, ports):
#     print("\n" + ' Starting Scan For ' + str(target))
#     nm = nmap.PortScanner()
#     nm.scan(target, str(ports))
#     for host in nm.all_hosts():
#         for proto in nm[host].all_protocols():
#             for port in nm[host][proto]:
#                 state = nm[host][proto][port]['state']
#                 product = nm[host][proto][port]['product']
#                 version = nm[host][proto][port]['version']
#                 print(f"[{port}/{proto}] {state} {product} {version}")

# def scan_port(ipaddress, port):
#     try:
#         sock = socket.socket()
#         sock.connect((ipaddress, port))
#         print("[+] Port Opened "+ str(port))
#         sock.close()
#     except:
#         pass

# targets = input("[*] Enter Targets to Scan(split them by ,): ")
# ports = int(input("[*] Enter How Many Ports You Want to Scan: "))
# if ',' in targets:
#     print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
#     for ip_addr in targets.split(","):
#         scan(ip_addr.strip(" "), ports)
# else:
#     scan(targets, ports)