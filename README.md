# 🛡️ File Integrity Monitor - Web Version (Auto-Refresh)

A simple **File Integrity Monitoring** tool built in **Python** with a **Flask web interface**.  
It monitors a given folder for **file creations, deletions, and modifications**, logs all events, and displays them in a clean web dashboard with **automatic updates**.

---

## 📌 Features
- 📂 Monitors a specific folder for changes.
- 📝 Detects:
  - File creation
  - File deletion
  - File modification (content changes)
- 🌐 Web dashboard to view file change logs.
- ⏱ **Auto-refresh every 5 seconds** — see changes live.
- 📄 All changes logged to `logs.txt` for permanent records.
- 🔄 Runs in real-time in the background.

---

## 🛠️ Technologies Used
- **Python 3**
- [Flask](https://flask.palletsprojects.com/)
- [Watchdog](https://pypi.org/project/watchdog/)
- HTML + CSS (for web UI)

---

## 🚀 Setup & Run

### 1️⃣ Install Requirements
Make sure Python 3 is installed. Then, open a terminal in the project folder and run:
```bash
pip install flask watchdog
```
---

2️⃣ Prepare the Project Folder
Create a folder named test_folder in the project directory.

This is the folder that will be monitored for changes.

3️⃣ Run the Application

```bash
python app.py
```
---

4️⃣ View the Dashboard

Open your browser and go to:

http://127.0.0.1:5000

---

The dashboard will auto-refresh every 5 seconds to display the latest changes.

🧪 Testing the Monitor
Open the test_folder.

Create a new file → Dashboard shows File Created.

Edit an existing file → Dashboard shows File Modified.

Delete a file → Dashboard shows File Deleted.

---

📜 How It Works
Uses Watchdog to listen for file system events in test_folder.

Calculates SHA256 hash of each file to detect content changes.

Logs all changes to logs.txt.

Flask serves the log data in a web interface with auto-refresh.

🔮 Future Work
📩 Email & Telegram alerts for critical file changes.

📊 Search and filter options in the web UI to find specific events.

📥 Export logs as CSV or PDF for reporting purposes.

📂 Multi-folder monitoring support.

🗄 Database storage (SQLite/MySQL) instead of plain text logs.

🔐 User authentication for secure web access.

🌍 Remote monitoring over the internet with secure access control.

⚠️ Disclaimer
This tool is for educational and testing purposes only.
Do NOT use it to monitor or interfere with systems you do not own or have permission to monitor.
