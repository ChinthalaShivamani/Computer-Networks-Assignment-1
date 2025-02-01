from scapy.all import rdpcap

pcap_file = "8.pcap"
packets = rdpcap(pcap_file)

unique_packets = set()

for packet in packets:
    if packet.haslayer("TCP"):  
        ack_number = packet["TCP"].ack  
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst

        if 1678999000 <= ack_number <= 1700000000:
            unique_packets.add((src_ip, dst_ip, ack_number))

print(f"Total unique packets found: {len(unique_packets)}")
for src_ip, dst_ip, ack_number in unique_packets:
    print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Ack Number: {ack_number}")
