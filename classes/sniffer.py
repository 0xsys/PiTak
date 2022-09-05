from scapy.all import *

class sniffer:
    
    # Berkley Packet Filter, Time to Live (Number of packets)
    def __init__(self, bpf, nop):
        self.filter = bpf
        self.numberOfPackets = nop

    def sniffPrint(self, packet):
        packet.show()

    def sniffToTerminal(self):
        sniff(filter = self.filter, prn = self.sniffPrint)