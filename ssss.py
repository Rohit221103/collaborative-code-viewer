import subprocess
from subprocess import PIPE
from getpass import getpass
def get_connected_devices():
    ips=[]
    with open('b.text','w') as f:
        try:
            x=getpass("password: ")
            arp_table = subprocess.Popen(['sudo','-S','arp-scan','-l','--retry','5'],stdin=PIPE,stdout=f) 
        except subprocess.CalledProcessError:
            print("Error: Unable to retrieve ARP table.")
    with open('b.text','r') as f:
        x=f.readline()
        print(x)
        y=[i for i in x if ('.' in i[:4])]
        z=[i.split()[:2] for i in y]
        print(x)
        w=[]
        for i in z:
            if i not in w:
                w.append(i)
            
    print(w)


if __name__ == "__main__":
    connected_devices = get_connected_devices()


'''import scapy.all as scapy

class scan:
    def Arp(self, ip):
        self.ip = ip
        print(ip)
        arp_r = scapy.ARP(pdst=ip)
        br = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        request = br/arp_r
        answered, unanswered = scapy.srp(scapy.Ether(dst = "FF:FF:FF:FF:FF:FF") / scapy.ARP(pdst = ip), timeout = 1, iface = 'wlp1s0', inter = 0.1)

        print('\tIP\t\t\t\t\tMAC')
        print('_' * 37)
        for i in answered:
            ip, mac = i[1].psrc, i[1].hwsrc
            print(ip, '\t\t' + mac)
            print('-' * 37)

arp = scan() # create an instance of the class
arp.Arp('192.168.0.1/24') 
import sys
from datetime import datetime
from scapy.all import srp,Ether,ARP,conf 
import nmap


def arp_scan(interface, ips):

	print("[*] Scanning...") 
	start_time = datetime.now()

	conf.verb = 0 
	ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), 
		     timeout = 2, 
		     iface = interface,
		     inter = 0.1)

	print ("\n[*] IP - MAC") 
	for snd,rcv in ans: 
		print(rcv.sprintf(r"%ARP.psrc% - %Ether.src%"))
	stop_time = datetime.now()
	total_time = stop_time - start_time 
	print("\n[*] Scan Complete. Duration:", total_time)

if __name__ == "__main__":
    arp_scan(sys.argv[1], sys.argv[2])
import scapy.all as scapy

def scan(ip):
    # Create ARP request packet
    arp_request = scapy.ARP(pdst=ip)

    # Create Ethernet frame to broadcast the ARP request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine the Ethernet frame and the ARP request packet
    arp_request_broadcast = broadcast / arp_request

    # Send the packet and receive responses
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # List to store the IP addresses
    clients_list = []

    # Extract IP and MAC addresses from responses
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

# Specify your network range (e.g., 192.168.1.0/24)
network = "192.168.160.0/24"
scan_result = scan(network)
print_result(scan_result)'''