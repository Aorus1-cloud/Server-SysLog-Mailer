# 🖥️ Server-SysLog-Mailer 

> Automated server health monitor that logs system metrics and emails detailed reports on a configurable schedule.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![psutil](https://img.shields.io/badge/psutil-5.x-4CAF50?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey?style=for-the-badge&logo=linux&logoColor=white)

---

## 📌 Overview

**Server-SysLog-Mailer ** is a lightweight, scheduled system monitoring CLI tool built with Python.  
It captures a full snapshot of your server's health — CPU, RAM, disk, network, and the  
top 10 most memory-hungry processes — writes a structured `.log` file, and automatically  
delivers it to your inbox via Gmail SMTP.

---

## ✨ Features

- 📊 **CPU & RAM monitoring** — real-time usage percentages
- 💾 **Disk partition reporting** — usage across all mounted partitions
- 🌐 **Network I/O tracking** — bytes sent and received (in MB)
- 🔥 **Top 10 hot processes** — ranked by RAM usage with full details
- 🧵 **Per-process metadata** — PID, owner, threads, open files, virtual memory
- 📁 **Timestamped log files** — auto-saved to a configurable directory
- 📧 **Email delivery** — log sent as `.log` attachment via Gmail SMTP
- ⏱️ **Scheduled execution** — configurable polling interval in minutes

---

## 🧰 Dependencies

| Package | Purpose | Install |
|---|---|---|
| ![Python](https://img.shields.io/badge/-Python_3.8+-3776AB?logo=python&logoColor=white) | Runtime | [python.org](https://www.python.org/downloads/) |
| `psutil` | System & process metrics | `pip install psutil` |
| `schedule` | Job scheduling | `pip install schedule` |
| `python-dotenv` | Load .env credentials | `pip install python-dotenv` |
| `smtplib` | Email via SMTP | ✅ Built-in |
| `email` | Email message builder | ✅ Built-in |

Install all third-party dependencies at once:

```bash
pip install psutil schedule python-dotenv
```

---

## 📂 Project Structure
Server-SysLog-Mailer /
├── ServerProcessMonitoringModules.py # Core monitoring & email logic\
├── main.py # CLI entry point & scheduler\
├── logs/ # Auto-created log output directory\
├── requirements.txt\
└── README.md\


---

## 🚀 Usage

```bash
python main.py <log_dir> <interval_minutes>
```

### 📋 Arguments

| Argument | Description | Example |
|---|---|---|
| `log_dir` | Directory to save log files | `./logs` |
| `interval_minutes` | How often to run (in minutes) | `30` |

### 🔖 Flags

```bash
python ServerProcessMonitoringScript.py --h    # Help
python ServerProcessMonitoringScript.py --u    # Usage info
```

### ✅ Example

```bash
python ServerProcessMonitoringScript.py ./logs 30 
```

---

## 📧 Gmail Setup

Server-SysLog-Mailer  uses **Gmail App Passwords** — not your actual Gmail password.

1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Enable **2-Step Verification**
3. Navigate to **Security → App Passwords**
4. Generate a new password for "Mail"
5. Use that 16-character password as `gmail_app_password`

> ⚠️ Never commit your App Password to GitHub. Use environment variables or a `.env` file in production.

---

## 📄 Sample Log Output

------This is the log report of the system info of the server.----\

---------------------------System Report--------------------------\
CPU Usage : 14.3%%\
RAM Usage : 62.5%%\

Disk Usage Report\
/ -> 74.2%% used\

Network Usage Report\
Sent : 120.45 Mb\
Recv : 980.32 Mb\

------------------Top Memory Consuming Processes------------------\
PID : 1423\
Process Name : python3\
Owner : fedora\
CPU Usage : 2.30%%\
RAM Usage : 145.23 MB\
...
...
...


---

## ⚠️ Known Limitations

- Requires a Gmail account with App Passwords enabled
- Some process metrics may show `N/A` due to OS-level permission restrictions
- Designed for single-server use; not a distributed monitoring solution

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author
**Jayesh**  
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Aorus1-cloud)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jayesh-patil-b94108339/)