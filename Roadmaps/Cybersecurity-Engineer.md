# 🔐 Cybersecurity Engineer Roadmap (18 Months)

This roadmap acts as your command center for transitioning into a Cybersecurity Engineer role. It covers Red Team, Blue Team, and Cloud Security principles over 18 months.

---

## Phase 1: IT & Networking Foundations (Month 1-2)

### 🎯 Learning Focus

Understand the systems you are trying to protect (or break).

### 🛡️ Security Concepts

* **The Internet:** How data moves from A to B.
* **Ports & Protocols:** SSH (22), HTTP (80), HTTPS (443), DNS (53).
* **OS Fundamentals:** File permissions (chmod), Process management (ps, kill).

### 🔧 Tools to Master

* **Linux (Kali):** Command line is mandatory.
* **Wireshark:** Analyzing packet captures (.pcap).
* **VirtualBox/VMware:** Running isolated labs.

### 🧠 Theoretical Knowledge

* **OSI Model:** All 7 layers (Physical to Application).
* **TCP/IP:** Handshake (SYN, SYN-ACK, ACK).
* **IP Addressing:** IPv4, Subnetting, CIDR.

### 💻 Hands-On Labs

1. **Home Lab Setup:** Install Kali Linux and Metasploitable2 in VirtualBox. Ensure they can ping each other (Host-Only Adapter).
2. **Packet Sniffing:** Use Wireshark to capture your own browser traffic and identify the DNS request.
3. **Linux Hardening:** secure a Linux server by disabling root login and configuring UFW (Uncomplicated Firewall).

### 🚩 CTF / Practice Platforms

* **TryHackMe:** Pre-Security Path.
* **OverTheWire:** Bandit (Linux basics).

### 📚 Learning Resources

* **Course:** [Google Cybersecurity Professional Certificate (Coursera)](https://www.coursera.org/professional-certificates/google-cybersecurity)
* **Book:** Comptia Network+ Certification Guide.

### ✅ Phase Completion Goals

You can analyze a network packet and comfortably navigate the Linux terminal.

---

## Phase 2: Security Fundamentals (Month 3-4)

### 🎯 Learning Focus

The core principles of information security.

### 🛡️ Security Concepts

* **CIA Triad:** Confidentiality, Integrity, Availability.
* **AAA:** Authentication, Authorization, Accounting.
* **Cryptography:** Symmetric (AES) vs Asymmetric (RSA), Hashing (SHA-256).

### 🔧 Tools to Master

* **Nmap:** Network mapping and port scanning.
* **Netcat:** The TCP/IP Swiss Army Knife.
* **OpenSSL:** Inspecting certificates.

### 🧠 Theoretical Knowledge

* **Risk Management:** Asset value, Threats, Vulnerabilities.
* **Compliance:** GDPR, HIPAA basics.
* **PKI:** Public Key Infrastructure (Certificates, CAs).

### 💻 Hands-On Labs

1. **Nmap Scanning:** Scan your local network to find open ports. (Do NOT scan unauthorized networks).
2. **Encryption Lab:** Encrypt a file using GPG and decrypt it.
3. **Hash Cracking:** Create a hash of a password and try to identify the hash type.

### 🚩 CTF / Practice Platforms

* **TryHackMe:** Introduction to Cyber Security Path.
* **PicoCTF:** General Skills & Cryptography.

### 🏆 Certification Milestone

* **CompTIA Security+ (SY0-701)** - The industry entry standard.

### ⚖️ Legal & Ethical Notes

* **Authorization:** Never scan or exploit a system without written permission.

### ✅ Phase Completion Goals

You understand the vocabulary of security and pass a practice Security+ exam.

---

## Phase 3: Web Application Security (Month 5-6)

### 🎯 Learning Focus

Exploiting and defending web apps (where most attacks happen).

### 🛡️ Security Concepts

* **OWASP Top 10:** The bible of web vulnerabilities.
* **Injection:** SQLi, Command Injection.
* **XSS:** Stored vs Reflected Cross-Site Scripting.

### 🔧 Tools to Master

* **Burp Suite (Community):** Intercepting proxies.
* **OWASP ZAP:** Automated scanner.
* **Browser DevTools:** Inspecting source code.

### 🧠 Theoretical Knowledge

* **HTTP:** Methods (GET, POST, PUT), Headers, Cookies.
* **Same-Origin Policy (SOP).**
* **Secure Coding:** Input validation, Output encoding.

### 💻 Hands-On Labs

1. **SQL Injection:** Use DVWA (Damn Vulnerable Web App) to bypass a login page using `' OR 1=1 --`.
2. **Reflected XSS:** Execute `alert(1)` on a vulnerable search bar.
3. **Burp Proxy:** Intercept a request, modify the parameters, and forward it.

### 🚩 CTF / Practice Platforms

* **PortSwigger Web Security Academy:** (The best free resource for web security).
* **OWASP Juice Shop:** A broken modern web app.

### 📚 Learning Resources

* **Book:** The Web Application Hacker's Handbook.

### ✅ Phase Completion Goals

You can manually identify and exploit an SQL injection vulnerability.

---

## Phase 4: Network Security & Pentesting (Month 7-9)

### 🎯 Learning Focus

Offensive tactics to find weaknesses in infrastructure.

### 🛡️ Security Concepts

* **Ethical Hacking Lifecycle:** Recon -> Scanning -> Exploitation -> Post-Exploitation -> Reporting.
* **Privilege Escalation:** Going from user to root/admin.

### 🔧 Tools to Master

* **Metasploit:** Exploitation framework.
* **Nessus:** Vulnerability scanner.
* **Hydra/John the Ripper:** Password attacks.
* **Searchsploit:** Finding exploits.

### 🧠 Theoretical Knowledge

* **Vulnerability Assessment vs. Penetration Testing.**
* **CVSS Scores:** Identifying severity (Critical, High, Medium, Low).
* **Active Directory:** Basics of Windows domains (Kerberos, LDAP).

### 💻 Hands-On Labs

1. **Metasploitable Root:** Gain root access to your Metasploitable VM using a known vulnerability (e.g., vsftpd backdoor).
2. **Pass the Hash:** Understand how Windows authentication moves laterally.

### 🚩 CTF / Practice Platforms

* **HackTheBox (HTB):** Starting Point (Free Tier).
* **VulnHub:** Downloadable vulnerable machines.

### 🏆 Certification Milestone

* **eJPT (eLearnSecurity Junior Penetration Tester)** - Highly practical exam.

### ✅ Phase Completion Goals

You can obtain a reverse shell on a vulnerable machine in a controlled environment.

---

## Phase 5: Defensive Security & Incident Response (Month 10-12)

### 🎯 Learning Focus

Detecting attacks and stopping them (Blue Team).

### 🛡️ Security Concepts

* **Incident Response Lifecycle:** Preparation, Detection, Containment, Eradication, Recovery, Lessons Learned.
* **Kill Chain:** Stopping attacks at different stages.
* **IOCs:** Indicators of Compromise (Hash, IP, Domain).

### 🔧 Tools to Master

* **SIEM:** Splunk (Free Fundamentals), ELK Stack.
* **IDS/IPS:** Snort / Suricata.
* **EDR:** Endpoint Detection & Response concepts.

### 🧠 Theoretical Knowledge

* **Cyber Kill Chain (Lockheed Martin).**
* **MITRE ATT&CK Framework:** TTPs (Tactics, Techniques, and Procedures).
* **Digital Forensics:** Chain of custody, Volatility (Memory analysis).

### 💻 Hands-On Labs

1. **Log Analysis:** Ingest Apache logs into Splunk and query for 404/500 errors.
2. **Malware Analysis (Basic):** Analyze a suspicious PDF in a sandbox (Any.Run).
3. **Snort Rules:** Write a rule to alert on ICMP traffic.

### 🚩 CTF / Practice Platforms

* **Blue Team Labs Online (BTLO).**
* **LetsDefend.**

### 🏆 Certification Milestone

* **CompTIA CySA+ (Cybersecurity Analyst).**

### ✅ Phase Completion Goals

You can look at a log file and identify "Who, What, Where, When" of an attack.

---

## Phase 6: Cloud Security & DevSecOps (Month 13-15)

### 🎯 Learning Focus

Securing the modern infrastructure.

### 🛡️ Security Concepts

* **Shared Responsibility Model.**
* **Infrastructure as Code (IaC) Security.**
* **Container Security.**

### 🔧 Tools to Master

* **Cloud:** AWS IAM, Security Hub, GuardDuty.
* **Containers:** Docker, Kubernetes Security.
* **SAST/DAST:** SonarQube.

### 🧠 Theoretical Knowledge

* **DevSecOps:** Shifting security left.
* **Serverless Security.**
* **Cloud Misconfigurations:** S3 buckets public access.

### 💻 Hands-On Labs

1. **S3 Security:** Configure an S3 bucket with encryption and block public access.
2. **Vulnerable Infrastructure:** Deploy "CloudGoat" (Vulnerable AWS scenarios) and fix the flaws.

### 📚 Learning Resources

* **Docs:** AWS Security Documentation.
* **Course:** SANS Cloud Security Fundamentals (Expensive, look for cheaper alternatives like verify.cc).

### ✅ Phase Completion Goals

You can audit an AWS account for basic security flaws.

---

## Phase 7: Specialization (Month 16-18)

### 🎯 Learning Focus

Choosing your destiny.

**Option A: Red Team (Offensive)**

* **Focus:** Advanced Evasion, Active Directory, C2 Frameworks.
* **Cert:** OSCP (Offensive Security Certified Professional) - The "Gold Standard".

**Option B: Blue Team (Defensive)**

* **Focus:** Threat Hunting, Reverse Engineering, Forensics.
* **Cert:** BTL1 (Blue Team Level 1).

**Option C: GRC (Governance, Risk, Compliance)**

* **Focus:** Auditing, ISO 27001, Policy writing.
* **Cert:** CISA (Certified Information Systems Auditor).

---

## 🏗️ Getting Hired Strategy

### 🏠 Building a Home Lab

* **Hardware:** 16GB+ RAM Laptop to run 2-3 VMs simultaneously.
* **Network:** Separate VLAN for testing dangerous stuff (Optional but recommended).

### 📄 Portfolio

* **GitHub:** Scripts you wrote (Python/Bash).
* **Blog/Writeups:** *Crucial*. Solve a HTB box and write a walkthrough. "I found port 80 open, enumerating it revealed..."

### 🎤 Interview Prep

* **Scenario:** "You see a suspicious process on a server. Walk me through your response."
* **Technical:** "Explain the difference between TCP and UDP." "How does Traceroute work?"
* **Behavioral:** "Tell me about a time you had to deliver bad news (like a vulnerability)."

### 🐞 Bug Bounties

* Wait until you are comfortable with Phase 3/4.
* Start on **HackerOne** or **Bugcrowd**.
* Focus on "VDP" (Vulnerability Disclosure Programs) first—they pay in points/reputation, easier for beginners.

Stay legal, stay curious, and happy hacking! 🕵️‍♂️

---

*Last Updated: 2026-03-29*

![Kali Linux](https://img.shields.io/badge/Kali%20Linux-557C94?style=flat&logo=kalilinux&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=flat&logo=wireshark&logoColor=white)
![Metasploit](https://img.shields.io/badge/Metasploit-2596CD?style=flat&logoColor=white)
![Burp Suite](https://img.shields.io/badge/Burp%20Suite-FF6633?style=flat&logo=burpsuite&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonaws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## 💰 Salary & Job Market

* **Median Salary (US):** $95,000–$145,000/year (Junior to Mid-level)
* **Senior Security Engineer / CISO:** $145,000–$250,000+
* **Top Hiring Companies:** CrowdStrike, Palo Alto Networks, Mandiant (Google), Microsoft Security, government agencies (NSA, CISA), financial institutions, and every large enterprise
* **In-Demand Skills:** Penetration testing, cloud security (AWS/Azure), SIEM (Splunk), incident response, threat hunting, Python scripting, OSCP certification, DevSecOps
* **Job Market Note:** Cybersecurity has a significant talent shortage globally. The field is highly recession-resistant — security budgets are among the last to be cut. OSCP and cloud security certifications command the highest premiums.

## ⚠️ Common Mistakes

1. **Skipping the fundamentals to jump to "hacking"** — Developers who skip networking, Linux, and cryptography fundamentals and jump straight to Metasploit can run exploits but can't explain what they're doing or adapt when tools fail. Solid fundamentals are what separate professionals from script kiddies.
2. **Only focusing on offense (Red Team) or defense (Blue Team)** — The most effective security engineers understand both sides. Red teamers who don't understand detection are easier to catch; blue teamers who don't understand attack techniques miss threats. Study both, then specialize.
3. **Neglecting the legal and ethical boundaries** — Scanning or exploiting systems without explicit written authorization is illegal, regardless of intent. Always work in authorized lab environments (HackTheBox, TryHackMe, your own VMs). One unauthorized scan can end a career before it starts.
