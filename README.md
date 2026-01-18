# Network Traffic Analyzer (IDS)

## 🛡️ Project Overview
This is a **Blue Team** security project designed to monitor network traffic in real-time. It acts as a lightweight **Intrusion Detection System (IDS)** by capturing packets, parsing headers, and flagging potentially suspicious activity.

Building this project helped me understand the OSI model, packet encapsulation, and how automated logging works in a security operations center (SOC) environment.

## ✨ Features
* **Live Packet Sniffing:** Captures raw traffic using the `Scapy` library.
* **Protocol Analysis:** Extracts source/destination IPs and identifies TCP/UDP ports.
* **Security Alerting:** Detects unauthorized attempts on sensitive management ports (e.g., SSH, RDP).
* **Persistent Logging:** Automatically generates a `security_log.txt` file with timestamps for forensic review.

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Library:** Scapy
* **Environment:** Linux/Windows/macOS (requires administrative privileges)

## 🚀 How to Use
1. **Install Dependencies:**
   ```bash
   pip install scapy

```

2. **Run the Analyzer:**
*Note: Network sniffing requires root or administrator privileges.*
```bash
# On Linux/macOS
sudo python3 sniffer.py

# On Windows (Run Command Prompt as Administrator)
python sniffer.py

```


3. **View Results:**
Check the console for live alerts and refer to `security_log.txt` for the historical record of captured traffic.

## 📊 Sample Log Output

```text
[2026-01-18 17:53:48] --- LOG SESSION STARTED ---
[2026-01-18 17:53:48] Observed traffic from: 10.74.111.167
[2026-01-18 17:53:48] ALERT: Unauthorized access attempt on Port 3389 from 192.168.1.50

```

## 🧠 Future Improvements

* Add a GeoIP API to track the physical location of incoming traffic.
* Implement a visual dashboard using Matplotlib or a web interface.
* Add logic to detect "SYN Flood" DDoS attacks.

```

---

### Tips for your GitHub Repository:
1.  **Add a Screenshot:** If you can, take a screenshot of your terminal while the script is running and upload it to the repository. Seeing it in action makes people more likely to click.
2.  **Add a License:** When creating the repo on GitHub, choose the **MIT License**. it's standard for open-source projects.
3.  **Check your code for secrets:** Before you upload, make sure your code doesn't have your actual Wi-Fi passwords or sensitive personal info (though the script we wrote together is perfectly safe).

**Would you like me to show you how to add a "Visual Table" to your script so the terminal output looks even more professional before you upload it?**

```
