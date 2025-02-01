from scapy.all import rdpcap
import matplotlib.pyplot as plt
 
pcap_file = "8.pcap" 
packets = rdpcap(pcap_file)

src_flows = {}
dst_flows = {}
data_transferred = {}

for pckt in packets:
    if pckt.haslayer("IP"):
        src_ip = pckt["IP"].src
        dst_ip = pckt["IP"].dst
        packet_size = len(pckt)

        # Count flows for source IP
        if src_ip not in src_flows:
            src_flows[src_ip] = 0
        src_flows[src_ip] += 1

        # Count flows for destination IP
        if dst_ip not in dst_flows:
            dst_flows[dst_ip] = 0
        dst_flows[dst_ip] += 1

        # Handle source-destination data transfer
        if pckt.haslayer("TCP") or pckt.haslayer("UDP"):
            src_port = pckt["TCP"].sport if pckt.haslayer("TCP") else pckt["UDP"].sport
            dst_port = pckt["TCP"].dport if pckt.haslayer("TCP") else pckt["UDP"].dport
            flow = (f"{src_ip}:{src_port}", f"{dst_ip}:{dst_port}")
            
            if flow not in data_transferred:
                data_transferred[flow] = 0
            data_transferred[flow] += packet_size

# Find the source-destination pair with the most data transferred
max_flow = max(data_transferred, key=data_transferred.get)
max_data = data_transferred[max_flow]

# Display results
print("Source Flows (IP -> Total Flows):")
print(src_flows)

print("\nDestination Flows (IP -> Total Flows):")
print(dst_flows)

print("\nSource-Destination Pair with the Most Data Transferred:")
print(f"{max_flow[0]} -> {max_flow[1]}: {max_data} bytes")
