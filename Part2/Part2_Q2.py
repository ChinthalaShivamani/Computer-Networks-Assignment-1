from scapy.all import rdpcap

pcap_file = "8.pcap"
packets = rdpcap(pcap_file)

for pckt in packets:
    if pckt.haslayer("IP") and pckt.haslayer("TCP"):
        src_ip=pckt["IP"].src
        dst_ip=pckt["IP"].dst
        checksum=pckt["TCP"].chksum
        urgent_pointer=pckt["TCP"].urgptr
        seq_num=pckt["TCP"].seq

        checksum_hex_num= hex(checksum)[2:].zfill(4)
        seq_num_str = str(seq_num)

        if checksum_hex_num.startswith("b5") and urgent_pointer==0 and seq_num_str.endswith("6183"):
            print(f"Source IP:{src_ip}")
            print(f"Destination IP: {dst_ip}")
            print(f"Complete Checksum: 0x{checksum_hex_num}")