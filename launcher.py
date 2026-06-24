import os
import sys
import webbrowser
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

# --- AUTHORISED USERS ---
ALLOWED_USERS = ["mohammed.ali2", "admin", "jafar.al-tarouti", "mohammedahmedalisult"]

# --- EMBEDDED FILE LOGIC ---
if getattr(sys, 'frozen', False):
    # This path is used when running from the .exe
    BASE_DIR = Path(sys._MEIPASS)
else:
    # This path is used when running as a normal script
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
        webbrowser.open(HTML_FILE.absolute().as_uri())
    else:
        messagebox.showerror("Error", f"Embedded tool file not found at {HTML_FILE}")

if __name__ == "__main__":
    main()
