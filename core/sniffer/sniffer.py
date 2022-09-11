from scapy.all import *

class sniffer:
    
    # Berkeley Packet Filter defaults to None type, Packet count till stop (captures one on default)
    def __init__(self, bpf = None, pktNum = 1):
        self.filter = bpf
        self.numberOfPackets = pktNum

    # sniff() func needs to print through the prn feature which calls an outside function
    def sniffPrint(self, packet):
        packet.show()

    def sniffToTerminal(self):
        sniff(filter = self.filter, prn = self.sniffPrint)

    # Outputs captured packets to a .pcap file
    def sniffToFile(self):
        packets = sniff(filter = self.filter, count = self.numberOfPackets)
        wrpcap("sPiffer.pcap", packets)
 
x = sniffer()

x.sniffToTerminal()


