from socket import *
from termcolor import *
import sys

#Instantiate a socket object
main_socket = socket()

def mass_scan(ip_addresses, socket_obj, ports = 100, suppress_warnings = False):
    #If more than 1 IP entered, alert user that multiple are being checked.
    if len(ip_addresses) > 1:
        print(colored(
            "[*} Scanning multiple targets...", "green")
            )
    for ip_address in ip_addresses:
        #Print out current IP address being scanned.
        print(colored(
            f"[*] Checking address {ip_address}...", "yellow")
            )
        for port in range(1, ports):
            #Scan each port in given IP address, alert user to success/failure
            port_scan(ip_address, port, socket_obj, suppress_warnings)

def port_scan(ip_address, port, socket_obj, suppress_warnings = False):
    #Bundle IP and port number into destination tuple
    destination = (ip_address, port)

    try:
    #Make connection with socket object using destination tuple
        socket_obj.connect(destination)
        print(colored(
            f"[+] Connection successfully established to port: {port}.", "green")
            )
        socket_obj.close()
    except:
        #Only print warnings if suppress_warnings == True
        if not suppress_warnings:
            print(colored(
                f"[-] Port: {port} closed. Canceling.", "red")
                )

if (len(sys.argv) > 1):
    print(sys.argv)
    if "-s" in sys.argv:
        target_ips = sys.argv[sys.argv.index("-s") + 1].split(",")
        number_of_ports = int(sys.argv[sys.argv.index("-s") + 2])
else:
    #Grab user input
    target_ips = input(
                colored("[*] Enter IPs (comma separated): ", "yellow")
                )
    #Split user input into list
    target_ips = target_ips.split(",")
    number_of_ports = int(
                    input(
                    colored("[*] Enter number of ports to scan: ", "yellow")
                ))
                
mass_scan(target_ips, main_socket, number_of_ports, True)