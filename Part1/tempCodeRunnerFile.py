rc_port -dst_port) == 54286 and ack_flag and str(ack_number)[-4:0] == "1203":
            if str(ack_number)[-4:0] == "1203":
                print("Source IP:", src_ip)
                print("Destination IP:", dst_ip)
                print("Source Port:", src_port)
                print("Destination Port:", dst_port)
                print("ACK Flag:", ack_flag)
                print("ACK Number:", ack_number)