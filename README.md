# 🧠 TCP Three-Way Handshake Simulation

This project demonstrates how a **TCP connection is established** using the Three-Way Handshake process. It combines **Python socket programming**, **Scapy for custom packet crafting**, and **Wireshark** for real-world packet analysis.

---

## 📌 Project Objectives

- Understand the concept of the TCP three-way handshake
- Simulate TCP connections using Python sockets
- Craft raw TCP packets using Scapy
- Analyze real-time packet captures with Wireshark
- Document the full lifecycle of TCP connection establishment

---

## 🔄 What is TCP Three-Way Handshake?

The **TCP 3-way handshake** is a process to establish a reliable connection between a client and server.

1. **SYN**: Client sends a Synchronize request to server
2. **SYN-ACK**: Server acknowledges and responds with its own Synchronize
3. **ACK**: Client acknowledges the server's SYN-ACK

This ensures both ends agree on initial sequence numbers and communication can begin reliably.

---

## 🧰 Tools & Technologies Used

| Tool      | Purpose                                  |
|-----------|------------------------------------------|
| Python    | To simulate client-server TCP connections |
| Scapy     | For low-level TCP packet crafting         |
| Wireshark | To capture and analyze packet flows       |
| GitHub    | Version control and collaboration         |

---

## 📁 Project Structure

tcp-three-way-handshake/
├── socket_demo.py # Python socket client demo
├── scapy_simulation.py # Scapy-based packet crafting
├── report/
│ ├── TCP_Handshake_Report_Generated.pdf
│ └── TCP_Handshake_Slides_Generated.pptx
├── screenshots/
│ ├── syn.png
│ ├── syn_ack.png
│ └── ack.png
└── README.md

yaml
Copy
Edit

---

## 📄 Demo Code

### 🔹 socket_demo.py

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('example.com', 80))
print("Connection Established")
client.close()
🔹 scapy_simulation.py
python
Copy
Edit
from scapy.all import *

ip = IP(dst="192.168.1.1")
syn = TCP(dport=80, flags="S", seq=1000)
syn_ack = sr1(ip/syn)
ack = TCP(dport=80, flags="A", seq=syn_ack.ack, ack=syn_ack.seq + 1)
send(ip/ack)
🖼 Wireshark Packet Capture (Screenshots)
Step	Description	Screenshot
SYN	Client initiates connection	syn.png
SYN-ACK	Server responds with SYN-ACK	syn_ack.png
ACK	Client acknowledges connection	ack.png

📚 Report & Documentation
TCP_Handshake_Report_Generated.pdf – Detailed explanation of handshake theory and implementation

TCP_Handshake_Slides_Generated.pptx – Presentation-ready version

✅ Conclusion
This project provides both a conceptual and hands-on understanding of TCP connection establishment. It’s perfect for learning how low-level networking works and how real-world traffic behaves.

🔗 GitHub: [https://github.com/guru8014]



