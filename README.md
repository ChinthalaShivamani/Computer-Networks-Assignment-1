#Overview

This project contains several Python scripts that analyze .pcap network packet capture files using the Scapy library. The scripts analyze network packet data and generate results, such as packet size distribution, unique IP-port pairs, source and destination flows, TCP flags analysis, and more. The results of these analyses can be used for network troubleshooting, security analysis, and performance monitoring.

Requirements
To run these scripts, ensure that you have the following prerequisites:

Python 3.x: This project is developed using Python 3. Ensure that you have it installed.

Scapy: Scapy is a Python library used for packet manipulation. You can install it using the command:

bash
Copy
Edit
pip install scapy
Matplotlib: For visualizations, you need the Matplotlib library:

bash
Copy
Edit
pip install matplotlib
PCAP file: Ensure that you have a .pcap file (e.g., 8.pcap) for testing. The scripts expect this file to be located in the same directory as the Python scripts.

File Structure
plaintext
Copy
Edit
├── Part1_Q1.py            # Script for packet size analysis
├── Part1_Q2.py            # Script for extracting unique IP-port pairs
├── Part1_Q3.py            # Script for source-destination flow analysis
├── Part2_Q1.py            # Script for filtering TCP packets based on specific conditions
├── Part2_Q2.py            # Script for filtering TCP packets based on checksum and sequence number
├── Part2_Q3.py            # Script for counting packets with port sum between 10000 and 20000
├── Part2_Q4.py            # Script for filtering unique TCP packets with specific ACK number
├── 8.pcap                 # Example PCAP file to test scripts (ensure you have this file)
├── README.md              # This README file
