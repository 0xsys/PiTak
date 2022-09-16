from exfiltration import exfiltration

# Requires the .pcap file to be present otherwise will fail
# Run "sudo python3 snifferClassTest.py" and uncomment the .sniffToFile() line
a = exfiltration("/home/harrison/Programming/Repositories/sPiffer/core/sniffer/PiTak.pcap")
a.upload()