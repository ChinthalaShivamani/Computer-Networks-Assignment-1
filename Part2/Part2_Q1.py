
from scapy.all import rdpcap

pcap_file = "8.pcap"
packets=rdpcap(pcap_file)

for pckt in packets:
    if pckt.haslayer("IP") and pckt.haslayer("TCP"):
        src_ip = pckt["IP"].src
        dst_ip = pckt["IP"].dst
        src_port = pckt["TCP"].sport
        dst_port = pckt["TCP"].dport
        ack_flag = pckt["TCP"].flags & 0x10
        ack_number = pckt["TCP"].ack

        if abs(src_port - dst_port) == 54286 and ack_flag and str(ack_number).endswith("1203"):
            print(f"Source IP: {src_ip}")
            print(f"Destination IP: {dst_ip}")
            break