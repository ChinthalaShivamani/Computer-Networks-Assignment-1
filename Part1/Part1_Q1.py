from scapy.all import rdpcap
import matplotlib.pyplot as plt

# Load the .pcap file
pcap_file = "8.pcap"  # Here the .pcap file which we used
packets = rdpcap(pcap_file)

total_data = 0
packet_sizes = []

# Process packets
for pckt in packets:
    size = len(pckt)  
    total_data += size
    packet_sizes.append(size)

# Calculate metrics
total_packets = len(packet_sizes)
min_size = min(packet_sizes)
max_size = max(packet_sizes)
avg_size = total_data / total_packets

# Print metrics
print(f"Total Data Transferred: {total_data} bytes")
print(f"Total Packets Transferred: {total_packets}")
print(f"Minimum Packet Size: {min_size} bytes")
print(f"Maximum Packet Size: {max_size} bytes")
print(f"Average Packet Size: {avg_size:.2f} bytes")

# Plot the histogram
plt.hist(packet_sizes, bins=20, color='blue', edgecolor='black')
plt.title("Packet Size Distribution")
plt.xlabel("Packet Size (bytes)")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='', alpha=0.7)
plt.show()
