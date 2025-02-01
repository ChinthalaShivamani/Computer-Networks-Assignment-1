from scapy.all import rdpcap
import matplotlib.pyplot as plt

# Load the .pcap file   
pcap_file = "8.pcap"  # Here the .pcap file which we used
packets = rdpcap(pcap_file)
unique_pairs = set()

# Extract unique source and destination ports
for pckt in packets:
    if "IP" in pckt:
        src_ip = pckt["IP"].src
        dst_ip = pckt["IP"].dst
        if ("TCP" in pckt or "UDP" in pckt):
            src_port = pckt["TCP"].sport if "TCP" in pckt else pckt["UDP"].sport
            dst_port = pckt["TCP"].dport if "TCP" in pckt else pckt["UDP"].dport
            unique_pairs.add((f"{src_ip}:{src_port}", f"{dst_ip}:{dst_port}"))

# Print unique pairs  
print("Unique Pairs:")  
for src, dst in unique_pairs:
    print(f"{src} -> {dst}")