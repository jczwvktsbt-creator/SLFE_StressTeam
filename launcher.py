import os
import sys
import webview
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

# --- AUTHORISED USERS ---
ALLOWED_USERS = ["mohammed.ali2", "admin", "jafar.al-tarouti", "mohammedahmedalisult"]

# --- EMBEDDED FILE LOGIC ---
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).parent

HTML_FILE = BASE_DIR / "piping_loading_tool.html"

def get_windows_username():
    return os.environ.get("USERNAME", "").strip().lower()

def main():
    username = get_windows_username()
    if username not in [u.lower() for u in ALLOWED_USERS]:
        messagebox.showerror("Access Denied", f"User '{username}' is not authorised.")
        sys.exit(1)

    if HTML_FILE.exists():
        # Forces opening in a native app window, not a browser
        webview.create_window('Piping Loading Tool', str(HTML_FILE.absolute()))
        webview.start()
    else:
        messagebox.showerror("Error", f"Embedded tool file not found at {HTML_FILE}")

if __name__ == "__main__":
    main()
