# Packet Analysis Scripts

## Overview

This project contains several Python scripts that analyze .pcap network packet capture files using the **Scapy** library. The scripts analyze network packet data and generate results, such as packet size distribution, unique IP-port pairs, source and destination flows, TCP flags analysis, and more. The results of these analyses can be used for network troubleshooting, security analysis, and performance monitoring.

## Requirements

To run these scripts, ensure that you have the following prerequisites:

- **Python 3.x**: This project is developed using Python 3. Ensure that you have it installed.
- **Scapy**: Scapy is a Python library used for packet manipulation. You can install it using the command:

  
bash
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
Running the Scripts
Download and Prepare Environment:

Make sure you have Python installed on your machine.

Install the required dependencies using the following command:

bash
Copy
Edit
pip install scapy matplotlib
Download the PCAP File:

Ensure that you have a .pcap file (e.g., 8.pcap) located in the same directory as the scripts. If you don’t have this file, you can use any other .pcap file for testing, but make sure the file path is correct in the scripts.
Execute the Scripts:

To run each script, simply execute them from the command line or terminal. For example:

bash
Copy
Edit
python Part1_Q1.py
python Part1_Q2.py
python Part1_Q3.py
python Part2_Q1.py
python Part2_Q2.py
python Part2_Q3.py
python Part2_Q4.py
Each script will output specific results to the terminal or generate visualizations (e.g., histograms).

Detailed Script Descriptions
Part1_Q1.py: Packet Size Analysis
This script calculates the total data transferred, the total number of packets, and generates a histogram of packet sizes.

Results:
Total data transferred (bytes)
Total packets transferred
Minimum, maximum, and average packet size
Packet size distribution histogram
Part1_Q2.py: Unique IP-Port Pairs
This script extracts unique source and destination IP-port pairs from the .pcap file.

Results:
List of unique source-destination IP-port pairs
Part1_Q3.py: Source-Destination Flow Analysis
This script counts the number of flows for each source and destination IP, and identifies the source-destination pair with the most data transferred.

Results:
Number of flows for source and destination IPs
Source-destination pair with the most data transferred
Part2_Q1.py: TCP Packet Filter by Port and ACK Number
This script filters TCP packets with a specific source and destination port difference and a specific ACK number.

Results:
Source and destination IP for the packet that matches the conditions
Part2_Q2.py: TCP Packet Filter by Checksum and Sequence Number
This script filters TCP packets based on specific checksum and sequence number criteria.

Results:
Source and destination IP addresses
TCP checksum in hex format
Part2_Q3.py: Counting Packets with Port Sum Between 10000 and 20000
This script counts the number of packets where the sum of the source and destination ports lies between 10000 and 20000.

Results:
The number of packets meeting the port sum condition
Part2_Q4.py: Filtering Unique TCP Packets by ACK Number
This script filters TCP packets that have specific ACK numbers within a given range.

Results:
Source IP, destination IP, and ACK number for matching packets
Total number of unique packets found
Visualizations
For the scripts that generate visualizations, such as Part1_Q1.py, the generated graphs will appear in a new window using Matplotlib.

Example Output for Part1_Q1.py:
A histogram of packet sizes will be displayed.

Example text output:

plaintext
Copy
Edit
Total Data Transferred: 150000 bytes
Total Packets Transferred: 1200
Minimum Packet Size: 40 bytes
Maximum Packet Size: 1500 bytes
Average Packet Size: 125.00 bytes
Troubleshooting
File Not Found: Ensure that the .pcap file exists in the same directory as the scripts or adjust the file path in the script accordingly.
Dependencies Not Installed: If you encounter an error related to missing dependencies, make sure to install the necessary libraries using pip.
