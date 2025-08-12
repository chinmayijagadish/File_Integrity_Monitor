import time
import hashlib
import os
import threading
from flask import Flask, render_template
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# === Function to calculate file hash ===
def get_file_hash(file_path):
    """Return SHA256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except FileNotFoundError:
        return None

# === Event Handler ===
class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, file_hashes):
        self.file_hashes = file_hashes

    def log_change(self, action, file_path):
        log_msg = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {action}: {file_path}"
        print(log_msg)
        with open("logs.txt", "a") as log_file:
            log_file.write(log_msg + "\n")

    def on_created(self, event):
        if not event.is_directory:
            self.file_hashes[event.src_path] = get_file_hash(event.src_path)
            self.log_change("File Created", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.file_hashes.pop(event.src_path, None)
            self.log_change("File Deleted", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            new_hash = get_file_hash(event.src_path)
            if self.file_hashes.get(event.src_path) != new_hash:
                self.file_hashes[event.src_path] = new_hash
                self.log_change("File Modified", event.src_path)

# === Start File Monitor in Background ===
def start_monitor():
    folder_to_monitor = "test_folder"

    # Create folder if it doesn't exist
    if not os.path.exists(folder_to_monitor):
        os.makedirs(folder_to_monitor)

    # Store initial file hashes
    file_hashes = {}
    for root, _, files in os.walk(folder_to_monitor):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hashes[file_path] = get_file_hash(file_path)

    event_handler = FileChangeHandler(file_hashes)
    observer = Observer()
    observer.schedule(event_handler, folder_to_monitor, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# === Flask App ===
app = Flask(__name__)

@app.route("/")
def index():
    if not os.path.exists("logs.txt"):
        open("logs.txt", "w").close()
    with open("logs.txt", "r") as f:
        logs = f.readlines()
    logs = [log.strip() for log in logs if log.strip()]
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    monitor_thread = threading.Thread(target=start_monitor, daemon=True)
    monitor_thread.start()
    app.run(debug=True)
