from scapy.all import *

class sniffer:
    
    # Berkeley Packet Filter, Packet Count till stop
    def __init__(self, bpf, pktNum):
        self.filter = bpf
        self.numberOfPackets = pktNum

    def sniffPrint(self, packet):
        packet.show()

    def sniffToTerminal(self):
        sniff(filter = self.filter, prn = self.sniffPrint)

    def sniffToFile(self):
        packets = sniff(filter = self.filter, count = self.numberOfPackets)
        wrpcap("sPiffer.pcap", packets)