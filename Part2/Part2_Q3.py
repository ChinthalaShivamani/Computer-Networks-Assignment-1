from scapy.all import rdpcap

pcap_file = "8.pcap"
packets = rdpcap(pcap_file)

matched_packets=0

for pckt in packets :
    if pckt.haslayer("TCP") or pckt.haslayer("UDP") :
        src_port = pckt["TCP"].sport if pckt.haslayer("TCP") else pckt["UDP"].sport
        dst_port = pckt["TCP"].dport if pckt.haslayer("TCP") else pckt["UDP"].dport
        port_sum = src_port + dst_port

        if 10000<=port_sum<=20000:
            matched_packets+=1
print(f"Number of packets whose source and destinations ports sum is between 10000 and 20000: {matched_packets}")