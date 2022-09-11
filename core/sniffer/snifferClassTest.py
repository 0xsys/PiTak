from classes.add import sniffer

# use berkley packet filter for init of sniffer

x = sniffer("host 192.168.1.1 and ip", 200)

# Should print a stream of packets on terminal
#x.sniffToTerminal()

# Should output packets to a .pcap file.
#x.sniffToFile()