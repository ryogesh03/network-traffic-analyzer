from scapy.all import sniff, IP, TCP
from datetime import datetime
import os

# This line tells you EXACTLY where the file is being saved
print(f"File will be saved at: {os.getcwd()}/security_log.txt")

def write_to_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("security_log.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")

# Create the file immediately so you can see it
write_to_log("--- LOG SESSION STARTED ---")

def blue_team_monitor(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        
        # Rule: Log EVERY IP we see just to prove the log works
        log_entry = f"Observed traffic from: {src_ip}"
        write_to_log(log_entry)
        print(f"Logged: {src_ip}")

print("--- Blue Team IDS Shield: ACTIVE ---")
sniff(prn=blue_team_monitor, store=False, count=10) # Stops after 10 packets
print("Done! Check your folder now.")
